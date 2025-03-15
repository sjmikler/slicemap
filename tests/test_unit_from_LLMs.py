import pytest

from slicemap.slicemap import Slice, SliceMap


def slice_map_initialization():
    sm = SliceMap()
    assert len(sm) == 1
    assert sm.include == "start"
    assert sm.raise_missing is False


def slice_map_set_and_get_item():
    sm = SliceMap()
    sm[1:5] = "A"
    assert sm[2] == "A"
    assert sm[0] is None


def slice_map_set_and_get_item_with_end_include():
    sm = SliceMap(include="end")
    sm[1:5] = "A"
    assert sm[1] == "A"
    assert sm[5] is None


def slice_map_raise_key_error():
    sm = SliceMap(raise_missing=True)
    with pytest.raises(KeyError):
        _ = sm[0]


def slice_map_export():
    sm = SliceMap()
    sm[1:5] = "A"
    sm[5:10] = "B"
    exported = sm.export()
    assert exported == [
        Slice(-float("inf"), 1, None),
        Slice(1, 5, "A"),
        Slice(5, float("inf"), "B"),
    ]


def slice_map_copy():
    sm = SliceMap()
    sm[1:5] = "A"
    sm_copy = sm.copy()
    assert sm_copy[2] == "A"
    assert sm_copy is not sm


def slice_map_repr():
    sm = SliceMap()
    sm[1:5] = "A"
    sm[5:10] = "B"
    assert repr(sm) == "{[-inf,1): None, [1,5): A, [5,inf): B}"


def slice_map_plot_without_matplotlib():
    sm = SliceMap()
    with pytest.raises(ImportError):
        sm.plot()


def slice_map_returns_none_if_key_not_set():
    sm = SliceMap()
    assert sm[1] is None
    assert sm[2] is None
    assert sm[3] is None


def slice_map_raises_key_error_if_key_not_set_and_raise_missing_is_true():
    sm = SliceMap(raise_missing=True)
    with pytest.raises(KeyError):
        _ = sm[1]
    with pytest.raises(KeyError):
        _ = sm[2]
    with pytest.raises(KeyError):
        _ = sm[3]


def slice_map_returns_correct_value_for_slice():
    sm = SliceMap()
    sm[1:3] = "a"
    assert sm[1.5] == "a"
    assert sm[2.5] == "a"


def slice_map_returns_correct_value_after_multiple_overlapping_sets():
    sm = SliceMap()
    sm[1:5] = "a"
    sm[2:4] = "b"
    assert sm[1.5] == "a"
    assert sm[2.5] == "b"
    assert sm[3.5] == "b"
    assert sm[4.5] == "a"


def slice_map_returns_correct_value_when_include_is_end():
    sm = SliceMap(include="end")
    sm[1:3] = "a"
    assert sm[1] is None
    assert sm[2] == "a"
    assert sm[3] is None


def slice_map_returns_correct_length():
    sm = SliceMap()
    sm[1:3] = "a"
    assert len(sm) == 1
    sm[3:5] = "b"
    assert len(sm) == 2
    sm[1.5:4.5] = "c"
    assert len(sm) == 2


def slice_map_returns_correct_slice_at_key():
    sm = SliceMap()
    sm[1:3] = "a"
    slice_at_2 = sm.get_slice_at(2)
    assert slice_at_2.start == 1
    assert slice_at_2.end == 3
    assert slice_at_2.value == "a"


def slice_map_copy_returns_equal_slice_map():
    sm = SliceMap()
    sm[1:3] = "a"
    sm[3:5] = "b"
    sm_copy = sm.copy()
    assert sm_copy[1.5] == "a"
    assert sm_copy[2.5] == "a"
    assert sm_copy[3.5] == "b"
    assert sm_copy[4.5] == "b"
    assert len(sm_copy) == 2


def slice_map_export_returns_correct_list_of_slices():
    sm = SliceMap()
    sm[1:3] = "a"
    sm[3:5] = "b"
    exported = sm.export()
    assert exported[0].start == -float("inf")
    assert exported[0].end == 1
    assert exported[0].value is None
    assert exported[1].start == 1
    assert exported[1].end == 3
    assert exported[1].value == "a"
    assert exported[2].start == 3
    assert exported[2].end == 5
    assert exported[2].value == "b"
    assert len(exported) == 3


def slice_map_set_item_with_none_start_sets_negative_infinity():
    sm = SliceMap()
    sm[None:3] = "a"
    assert sm[-float("inf")] == "a"
    assert sm[1] == "a"
    assert sm[2] == "a"


def slice_map_set_item_with_none_stop_sets_infinity():
    sm = SliceMap()
    sm[1:None] = "a"
    assert sm[1] == "a"
    assert sm[100] == "a"
    assert sm[float("inf")] == "a"


def slice_map_getitem_with_slice_returns_tuple_of_values():
    sm = SliceMap()
    sm[1:3] = "a"
    sm[3:5] = "b"
    values = sm[1:5]
    assert values == ("a", "a", "b", "b")


def slice_map_getitem_with_slice_and_none_start_returns_tuple_from_negative_infinity():
    sm = SliceMap()
    sm[1:3] = "a"
    sm[3:5] = "b"
    values = sm[None:5]
    assert values == (None, "a", "a", "b", "b")


def slice_map_getitem_with_slice_and_none_stop_returns_tuple_to_infinity():
    sm = SliceMap()
    sm[1:3] = "a"
    sm[3:5] = "b"
    values = sm[1:None]
    assert values == ("a", "a", "b", "b", None)


def slice_map_getitem_with_infinity_returns_last_value():
    sm = SliceMap()
    sm[1:3] = "a"
    assert sm[float("inf")] is None


def slice_map_getitem_with_negative_infinity_returns_first_value():
    sm = SliceMap()
    sm[1:3] = "a"
    assert sm[-float("inf")] is None


def slice_map_get_slice_at_with_infinity_returns_last_slice():
    sm = SliceMap()
    sm[1:3] = "a"
    slice_at_inf = sm.get_slice_at(float("inf"))
    assert slice_at_inf.start == 3
    assert slice_at_inf.end == float("inf")
    assert slice_at_inf.value is None


def slice_map_get_slice_at_with_negative_infinity_returns_first_slice():
    sm = SliceMap()
    sm[1:3] = "a"
    slice_at_neg_inf = sm.get_slice_at(-float("inf"))
    assert slice_at_neg_inf.start == -float("inf")
    assert slice_at_neg_inf.end == 1
    assert slice_at_neg_inf.value is None


def slice_map_repr_returns_correct_string_representation():
    sm = SliceMap()
    sm[1:3] = "a"
    sm[3:5] = "b"
    assert repr(sm) == "{[-inf,1): None, [1,3): a, [3,5): b, [5,inf]: None}"


def slice_map_repr_returns_correct_string_representation_when_include_is_end():
    sm = SliceMap(include="end")
    sm[1:3] = "a"
    assert repr(sm) == "{[-inf,1]: None, (1,3]: a, (3,inf]: None}"


def slice_map_set_empty_slice_does_nothing():
    sm = SliceMap()
    sm[3:3] = "a"
    assert len(sm) == 0


def slice_map_plot_does_not_raise_import_error_if_matplotlib_is_not_installed(caplog):
    sm = SliceMap()
    sm[1:3] = 1
    sm.plot()
    assert "SliceMap.plot requires matplotlib to be installed!" in caplog.text


def slice_map_plot_does_not_plot_if_slicemap_is_empty(mocker):
    sm = SliceMap()
    plot_slicemap = mocker.patch("slicemap.slicemap.plot_slicemap")
    sm.plot()
    plot_slicemap.assert_not_called()


def test_init_with_default_parameters():
    sm = SliceMap()
    assert len(sm) == 0
    assert sm[10] is None


def test_init_with_custom_parameters():
    sm = SliceMap(include="end", raise_missing=True)
    with pytest.raises(KeyError):
        _ = sm[10]


def test_setitem_adds_slice():
    sm = SliceMap()
    sm[10:20] = "value"
    assert sm[15] == "value"
    assert sm[5] is None
    assert sm[25] is None


def test_setitem_overwrites_existing_slice():
    sm = SliceMap()
    sm[10:20] = "value1"
    sm[15:25] = "value2"
    assert sm[12] == "value1"
    assert sm[18] == "value2"
    assert sm[22] == "value2"


def test_setitem_with_unbounded_ranges():
    sm = SliceMap()
    sm[:20] = "left_unbounded"
    sm[50:] = "right_unbounded"
    assert sm[-1000] == "left_unbounded"
    assert sm[10] == "left_unbounded"
    assert sm[1000] == "right_unbounded"
    assert sm[30] is None


def test_setitem_empty_slice_does_nothing():
    sm = SliceMap()
    sm[10:20] = "value"
    sm[25:20] = "ignored"
    assert len(sm) == 2
    assert sm[15] == "value"
    assert sm[19] == "value"
    assert sm[20] is None


def test_getitem_raises_keyerror_when_configured():
    sm = SliceMap(raise_missing=True)
    sm[10:20] = "value"
    assert sm[15] == "value"
    with pytest.raises(KeyError):
        _ = sm[25]


def test_getitem_with_slice_returns_tuple():
    sm = SliceMap()
    sm[10:20] = "A"
    sm[20:30] = "B"
    sm[30:40] = "C"
    assert sm[15:35] == ("A", "B", "C")


def test_getitem_with_include_start():
    sm = SliceMap(include="start")
    sm[10:20] = "A"
    sm[20:30] = "B"
    assert sm[10] == "A"
    assert sm[20] == "B"


def test_getitem_with_include_end():
    sm = SliceMap(include="end")
    sm[10:20] = "A"
    sm[20:30] = "B"
    assert sm[10] is None
    assert sm[10 + 1e-6] == "A"
    assert sm[20] == "A"


def test_getitem_with_infinity():
    sm = SliceMap()
    sm[10:20] = "A"
    sm[20 : float("inf")] = "B"
    assert sm[float("inf")] == "B"
    sm[-float("inf") : 10] = "C"
    assert sm[-float("inf")] == "C"


def test_len_reflects_actual_slices():
    sm = SliceMap()
    assert len(sm) == 0
    sm[10:20] = "A"
    assert len(sm) == 2
    sm[20:30] = "B"
    assert len(sm) == 3
    sm[15:25] = "C"  # Overlaps with both previous slices
    assert len(sm) == 4


def test_export_returns_slice_list():
    sm = SliceMap()
    sm[10:20] = "A"
    sm[20:30] = "B"

    expected = [
        Slice(-float("inf"), 10, None),
        Slice(10, 20, "A"),
        Slice(20, 30, "B"),
        Slice(30, float("inf"), None),
    ]

    assert sm.export() == expected


def test_copy_creates_independent_instance():
    sm1 = SliceMap()
    sm1[10:20] = "A"

    sm2 = sm1.copy()
    sm2[10:20] = "B"

    assert sm1[15] == "A"
    assert sm2[15] == "B"


def test_get_slice_at_returns_correct_slice():
    sm = SliceMap()
    sm[10:20] = "A"
    sm[20:30] = "B"

    result = sm.get_slice_at(15)
    expected = Slice(10, 20, "A")

    assert result == expected


def test_repr_format():
    sm = SliceMap()
    sm[10:20] = "A"
    sm[20:30] = "B"

    expected = "{[-inf,10): None, [10,20): A, [20,30): B, [30,inf]: None}"
    assert repr(sm) == expected


def test_completely_overwriting_existing_slices():
    sm = SliceMap()
    sm[10:20] = "A"
    sm[20:30] = "B"
    sm[30:40] = "C"

    # Completely overwrites the previous slices
    sm[5:45] = "X"

    assert sm[15] == "X"
    assert sm[25] == "X"
    assert sm[35] == "X"
    assert len(sm) == 2
