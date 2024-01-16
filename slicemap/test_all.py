from .slicemap import SliceMap


def test_range_1():
    r = SliceMap()
    for i in range(10):
        r[i : i + 1] = i

    for i in range(10):
        assert r[i] == i


def test_range_2():
    r = SliceMap()
    for i in range(10000):
        r[i : i + 1] = i

    for i in range(10000):
        assert r[i] == i


def test_range_include_end_1():
    r = SliceMap(include="end")
    for i in reversed(range(10)):
        r[i : i + 1] = i

    for i in range(1, 10):
        assert r[i] == i - 1


def test_readme_example_1():
    sm = SliceMap()

    sm[-10:10] = 0
    sm[2:4] = 1
    sm[4:6] = 2
    sm[7:9] = 3
    sm[12:15] = 1.5
    assert sm[2] == 1
    assert sm[3] == 1
    assert sm[4] == 2
    assert sm[9] == 0
    assert sm[15] is None


def test_readme_example_2():
    sm1 = SliceMap(include="start")
    sm1[2:3] = 1
    sm1[3:4] = 2
    sm1[4:5] = 3
    assert sm1[3] == 2
    assert sm1[4] == 3

    sm2 = SliceMap(include="end")
    sm2[2:3] = 1
    sm2[3:4] = 2
    sm2[4:5] = 3
    assert sm2[3] == 1
    assert sm2[4] == 2


def test_readme_example_3():
    sm = SliceMap(include="start")

    sm[-10:10] = 0
    sm[2:4] = 1
    sm[4:6] = 2
    sm[7:9] = 3
    sm[12:15] = 1.5
    assert sm[3] == 1
    assert sm[5] == 2
    assert sm[8] == 3
    assert sm[3:8] == (1, 2, 0, 3)
    assert sm[:] == (None, 0, 1, 2, 0, 3, 0, None, 1.5, None)


def test_readme_example_4():
    inputs = [
        [1, 11, 5],
        [2, 6, 7],
        [3, 13, 9],
        [12, 7, 16],
        [14, 3, 25],
        [19, 18, 22],
        [23, 13, 29],
        [24, 4, 28],
    ]

    sm = SliceMap()
    sm[:] = 0

    for left, value, right in sorted(inputs, key=lambda x: x[1]):
        sm[left:right] = value

    assert sm.export() == [
        (-float("inf"), 1, 0),
        (1, 3, 11),
        (3, 9, 13),
        (9, 12, 0),
        (12, 16, 7),
        (16, 19, 3),
        (19, 22, 18),
        (22, 23, 3),
        (23, 29, 13),
        (29, float("inf"), 0),
    ]


def test_raising_oob():
    sm = SliceMap(include="start", raise_missing=True)
    sm[2:3] = 1
    sm[3:4] = 2
    sm[4:5] = 3
    sm[8:9] = 4

    assert sm[2] == 1
    assert sm[3] == 2
    assert sm[4] == 3
    assert sm[8] == 4

    test_keys = [-float("inf"), 0, 1, 5, 9, 100, float("inf")]
    for test_key in test_keys:
        try:
            _ = sm[test_key]
            raise AssertionError("KeyError not raised")
        except KeyError:
            pass

    sm = SliceMap(include="end", raise_missing=True)
    sm[2:3] = 1
    sm[3:4] = 2
    sm[4:5] = 3
    sm[8:9] = 4

    assert sm[3] == 1
    assert sm[4] == 2
    assert sm[5] == 3
    assert sm[9] == 4

    test_keys = [-float("inf"), 0, 1, 2, 8, 100, float("inf")]
    for test_key in test_keys:
        try:
            _ = sm[test_key]
            raise AssertionError("KeyError not raised")
        except KeyError:
            pass


def test_raising_oob_on_slices():
    sm = SliceMap(include="start", raise_missing=True)
    sm[2:3] = 1
    sm[3:4] = 2
    sm[4:5] = 3
    sm[8:9] = 4

    assert sm[2:4] == (1, 2, 3)

    test_keys = [
        slice(-float("inf"), 0),
        slice(0, 1),
        slice(1, 5),
        slice(2, 5),
        slice(2, 8),
        slice(5, 9),
        slice(8, 9),
        slice(9, 100),
        slice(100, float("inf")),
    ]
    for test_key in test_keys:
        try:
            _ = sm[test_key]
            raise AssertionError("KeyError not raised")
        except KeyError:
            pass

    sm = SliceMap(include="end", raise_missing=True)
    sm[2:3] = 1
    sm[3:4] = 2
    sm[4:5] = 3
    sm[8:9] = 4

    assert sm[3:5] == (1, 2, 3)

    test_keys = [
        slice(-float("inf"), 0),
        slice(0, 1),
        slice(1, 2),
        slice(2, 5),
        slice(2, 8),
        slice(3, 9),
        slice(8, 9),
        slice(8, 100),
        slice(100, float("inf")),
    ]
    for test_key in test_keys:
        try:
            _ = sm[test_key]
            raise AssertionError("KeyError not raised")
        except KeyError:
            pass


def test_slicing():
    sm = SliceMap(include="start", raise_missing=False)
    sm[2:3] = 1
    sm[3:4] = 2
    sm[4:5] = 3
    sm[8:9] = 4

    assert sm[2:4] == (1, 2, 3)
    assert sm[2:5] == (1, 2, 3, None)
    assert sm[2:8] == (1, 2, 3, None, 4)
    assert sm[2:9] == (1, 2, 3, None, 4, None)
    assert sm[2:10] == (1, 2, 3, None, 4, None)
    assert sm[2:] == (1, 2, 3, None, 4, None)
    assert sm[:9] == (None, 1, 2, 3, None, 4, None)
    assert sm[:] == (None, 1, 2, 3, None, 4, None)
