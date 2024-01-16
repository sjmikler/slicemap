# Quick Start

## Create, query and visualize SliceMap

```py
from slicemap import SliceMap

sm = SliceMap()

sm[-10:10] = 0
sm[2:4] = 1
sm[4:6] = 2
sm[7:9] = 3
sm[12:15] = 1.5
print(sm[2], sm[3], sm[4], sm[9], sm[15])
```

Outputs:

```
1 1 2 0 None
```

As long as you work with numerical values, you can do:

```
sm.plot()
```

![figure1](https://github.com/gahaalt/slicemap/blob/main/docs/figures/figure1.png?raw=true)

## Include `start` | `end`

The default value is `include="start"`, but you can choose to include the end of slices instead.

```py
from slicemap import SliceMap

sm1 = SliceMap(include="start")
sm1[2:3] = 1
sm1[3:4] = 2
sm1[4:5] = 3
print(sm1[3], sm1[4])

sm2 = SliceMap(include="end")
sm2[2:3] = 1
sm2[3:4] = 2
sm2[4:5] = 3
print(sm2[3], sm2[4])
```

Outputs:

```
2 3
1 2
```

## Query either values or ranges

You can equery each value individually, or query with a slice to get all values in given slice.

```py
from slicemap import SliceMap

sm = SliceMap(include="start")

sm[-10:10] = 0
sm[2:4] = 1
sm[4:6] = 2
sm[7:9] = 3
sm[12:15] = 1.5
print(sm[3], sm[5], sm[8])
print(sm[3:8])
print(sm[:])
```

Outputs:

```
1 2 3
(1, 2, 0, 3)
(None, 0, 1, 2, 0, 3, 0, None, 1.5, None)
```

## Other options

You can choose to raise `KeyError` when querying non-existing keys, or return `None` instead.
By default `None` is returned.

Example:

```py
from slicemap import SliceMap

sm = SliceMap(include="start", raise_missing=True)

sm[-10:10] = 0

try:
    print(sm[10])

    raise Exception("KeyError was not raised!")
except KeyError:
    print("KeyError was raised correctly!")
```

Outputs:

```
KeyError was raised correctly!
```    

---

You can use `get_slice_at` to get more information about the slice at given point:

```py
from slicemap import SliceMap

sm = SliceMap(include="start")

sm[-10:10] = 0
print(sm.get_slice_at(0))
```

Outputs:

```
Slice(start=-10, end=10, value=0)
```

## More information

* Package `matplotlib` is an optional dependency - without it you can use the pacakge, but not the plotting
  functionality.
* You can use slices based on any number-like objects (except complex numbers) as keys. It'll work with ints,
  floats or numpy values.
* You can use any object as values.
