from __future__ import annotations

import logging
from collections import namedtuple
from copy import deepcopy
from dataclasses import dataclass
from typing import Any, SupportsFloat

from sortedcontainers import SortedList


@dataclass
class Slicer:
    up_to_key: SupportsFloat
    value: Any = None
    missing: bool = False


Slice = namedtuple("Slice", ["start", "end", "value"])


class SliceMap:
    def __init__(
        self,
        include: str = "start",
        raise_missing: bool = False,
    ):
        """
        SliceMap is like dict that allows setting values for whole slices of keys.

        It is efficient, having O(log(n)) insertion and querying time complexity.
        Under the hood, it uses SortedList and bisect search to find the correct
        place for a key to insert.

        Parameters
        ----------
        include
            Either "start" or "end". If "start", the key on the threshold between
            two slices will belong to the second slice. If "end" it will belong to
            the first slice.
        raise_missing
            If True, accessing a key that was not set will raise KeyError. If False,
            accessing a key that was not set will return None.

        """
        assert include in ("start", "end"), "Possible `include` values: start | end"

        self.data = SortedList(key=lambda x: x.up_to_key)

        self.data.add(Slicer(up_to_key=float("inf"), value=None, missing=True))
        self.raise_missing = raise_missing
        self.include = include

    def copy(self) -> "SliceMap":
        """Returns a deepcopy of itself."""
        return deepcopy(self)

    def export(self) -> list[Slice]:
        """Export SliceMap as list of tuples.

        This allows using SliceMap's final slices in other parts of your program.
        """
        start_element = [Slice(-float("inf"), self.data[0].up_to_key, self.data[0].value)]
        elems = [Slice(p1.up_to_key, p2.up_to_key, p2.value) for p1, p2 in zip(self.data, self.data[1:])]
        return start_element + elems

    def __setitem__(self, slice_key: slice, value: Any) -> None:
        """Add a new slice to SliceMap. All values in slice key will map to the value.

        When adding new slice, a binary search will take place. This operation will
        have ``O(log(n))`` time complexity.

        Parameters
        ----------
        slice_key
            Slice of numerical values. If already exists in SliceMap, overlapping
            values will be overwritten. If, as a result of adding new slice, an
            existing slice will be 100% covered, it'll be removed.
        value
            Any python object can be a value.
        """
        assert isinstance(slice_key, slice)
        assert slice_key.step == 1 or slice_key.step is None

        start = slice_key.start if slice_key.start is not None else -float("inf")
        stop = slice_key.stop if slice_key.stop is not None else float("inf")

        logging.debug("Inserting value %s between keys %s:%s", value, start, stop)
        if start >= stop:
            logging.debug("Empty slice")
            return

        start_key_idx = self.data.bisect_left(Slicer(up_to_key=start))
        end_key_idx = self.data.bisect_right(Slicer(up_to_key=stop))
        if start_key_idx < len(self.data):
            old_value_to_keep = self.data[start_key_idx].value
            old_missing = self.data[start_key_idx].missing
        else:
            old_value_to_keep = None
            old_missing = True
        num_el_to_remove = end_key_idx - start_key_idx

        logging.debug("Will remove %s values", num_el_to_remove)

        for _ in range(num_el_to_remove):
            logging.debug(
                "Removing value %s up to key %s",
                self.data[start_key_idx].value,
                self.data[start_key_idx].up_to_key,
            )
            self.data.pop(start_key_idx)

        logging.debug("Inserting value %s up to key %s", old_value_to_keep, start)
        logging.debug("Inserting value %s up to key %s", value, stop)
        if start > -float("inf"):
            self.data.add(Slicer(up_to_key=start, value=old_value_to_keep, missing=old_missing))
        self.data.add(Slicer(up_to_key=stop, value=value, missing=False))

    def __getitem__(self, key: SupportsFloat | slice) -> Any:
        """Check the value under the given key.

        If there's none and ``raise_missing`` was set to False during SliceMap
        initialization, None will be returned.

        Parameters
        ----------
        key
            A numerical key value.

        Returns
        -------
        Any
            Value of the key or None (if key is not present in SliceMap).

        Raises
        ------
        KeyError
            If ``raise_missing`` was set to True during SliceMap initialization,
            KeyError will be raised when trying to access a key that was not set.

        """
        if key == float("inf"):
            return self._maybe_get_value(self.data[-1], key)
        if key == -float("inf"):
            return self._maybe_get_value(self.data[0], key)

        if self.include == "start":
            search_op = self.data.bisect_right
        else:
            search_op = self.data.bisect_left

        if isinstance(key, slice):
            if key.start == -float("inf") or key.start is None:
                idx1 = 0
            else:
                idx1 = search_op(Slicer(up_to_key=key.start))

            if key.stop == float("inf") or key.stop is None:
                idx2 = len(self.data) - 1
            else:
                idx2 = search_op(Slicer(up_to_key=key.stop))

            return tuple(self._maybe_get_value(self.data[i], key) for i in range(idx1, idx2 + 1))
        else:
            idx = search_op(Slicer(up_to_key=key))
            return self._maybe_get_value(self.data[idx], key)

    def _maybe_get_value(self, pair: Slicer, key: SupportsFloat | slice):
        if self.raise_missing and pair.missing:
            raise KeyError(f"Key {key} not set in SliceMap!")
        return pair.value

    def get_slice_at(self, key: SupportsFloat) -> Slice:
        """Check the slice at the given key."""

        if self.__len__() == 0:
            return Slice(-float("inf"), self.data[0].up_to_key, self.data[0].value)
        if key == float("inf"):
            return Slice(self.data[-2].up_to_key, self.data[-1].up_to_key, self.data[-1].value)
        if key == -float("inf"):
            return Slice(-float("inf"), self.data[0].up_to_key, self.data[0].value)

        if self.include == "start":
            search_op = self.data.bisect_right
        else:
            search_op = self.data.bisect_left

        idx = search_op(Slicer(up_to_key=key))
        return Slice(self.data[idx - 1].up_to_key, self.data[idx].up_to_key, self.data[idx].value)

    def __len__(self) -> int:
        """Return the number of slices in SliceMap.

        If a slice becomes redundant because other slices are covering it 100%,
        it is removed from the SliceMap, and length might decrease.

        Returns
        -------
        int
            The number of slices in SliceMap.
        """
        return len(self.data) - 1

    def __repr__(self) -> str:
        start_bracket = "[" if self.include == "start" else "("
        end_bracket = ")" if self.include == "start" else "]"

        values = []

        p = self.data[0]
        if p is self.data[-1]:
            end_bracket = "]"

        values.append(f"[-inf,{p.up_to_key}{end_bracket}: {p.value}")

        for p1, p2 in zip(self.data, self.data[1:]):
            if p2 is self.data[-1]:
                end_bracket = "]"

            values.append(f"{start_bracket}{p1.up_to_key},{p2.up_to_key}" f"{end_bracket}: {p2.value}")

        return "{" + ", ".join(values) + "}"

    def plot(self) -> None:
        """If values are numerical and matplotlib is installed: plots SliceMap."""
        try:
            from slicemap import plot_slicemap

            return plot_slicemap(self) if len(self) > 0 else None
        except ImportError:
            logging.error("SliceMap.plot requires matplotlib to be installed! Run `pip install matplotlib`")
