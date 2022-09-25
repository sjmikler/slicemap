from slicemap import SliceMap


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
