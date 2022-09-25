SliceMap is similar to a normal Python dict, but instead of setting values key by key, you set entire slices at once.

This is a useful data structure implemented entirely in Python with help of `sortedcontainers` package.
Initially, I used a custom skip-list implementation, but this wasn't as fast as `sortedcontainers`
([see their benchmarks](https://grantjenks.com/docs/sortedcontainers/performance-scale.html)).

Adding new ranges and querying values both have `O(log(n))` time complexity.

# Quick Start

### Installation [![PyPI version](https://badge.fury.io/py/slicemap.svg)](https://badge.fury.io/py/slicemap)

```
pip install slicemap
```

### Create, query and visualize SliceMap

```
from slicemap import SliceMap
sm = SliceMap()

sm[-10:10] = 0
sm[2:4] = 1
sm[4:6] = 2
sm[7:9] = 3
sm[12:15] = 1.5
print(sm[2], sm[3], sm[4], sm[9], sm[15])

# works only for numeric values
sm.plot() 
```

Outputs:

```
1 1 2 0 None
```

![figure1](https://github.com/gahaalt/slicemap/blob/main/figures/figure1.png?raw=true)

### Include `start` | `end`

The default value is `include="start"`. But you can include the end of each slice instead.

```
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

### Query either values or ranges

You can equery each value individually, or query with a slice to get all values in given slice.

```
from slicemap import SliceMap
sm = SliceMap(include="start")

sm[-10:10] = 0
sm[2:4] = 1
sm[4:6] = 2
sm[7:9] = 3
sm[12:15] = 1.5
print(sm[3], sm[5], sm[8])
print(sm[3:8])
```

Outputs:

```
1 2 3
(1, 2, 0, 3)
```

# Applications

### [The Skyline Problem](https://www.geeksforgeeks.org/the-skyline-problem-set-2/)

Easily solvable in `O(n*log(n))` time:

```
from slicemap import SliceMap

# format [left_x, value, right_x]
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

print(sm)
print(sm.export())
sm.plot()
```

Outputs:

```
{(-inf,1): 0, [1,3): 11, [3,9): 13, [9,12): 0, [12,16): 7, [16,19): 3, [19,22): 18, [22,23): 3, [23,29): 13, [29,inf): 0}
[(-inf, 1, 0), (1, 3, 11), (3, 9, 13), (9, 12, 0), (12, 16, 7), (16, 19, 3), (19, 22, 18), (22, 23, 3), (23, 29, 13), (29, inf, 0)]
```

![figure2](https://github.com/gahaalt/slicemap/blob/main/figures/figure2.png?raw=true)

Depending on the exact task formulation, answer should be easy to retrieve from the above.

# Answers

* Package `matplotlib` is an optional dependency - without it you can use the pacakge, but not the plotting functionality.
