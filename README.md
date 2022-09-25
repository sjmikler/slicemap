[![PyPI version](https://badge.fury.io/py/slicemap.svg)](https://badge.fury.io/py/slicemap)

This is a useful data structure implemented entirely in Python with help of `sortedcontainers` package.
Initially, I used a custom skip-list implementation, but this wasn't as fast as `sortedcontainers`
([see benchmarks](https://grantjenks.com/docs/sortedcontainers/performance-scale.html)).
SliceDict is similar to a normal Python dict, but instead of setting values key by key, you set entire slices at once.

Adding new ranges and querying values both have `O(log(n))` time complexity.

# Quick Start

### Create, query and visualize SliceMap

```
from slicemap import SliceMap
sm = SliceMap(inlcude="start")

sm[-10:10] = 0
sm[2:4] = 1
sm[4:6] = 2
sm[7:9] = 3
sm[12:15] = 1.5
print(sm[2], sm[3], sm[4], sm[9], sm[15])
sm.plot()  # works only for numeric values
```

Outputs:

```
1 1 2 0 None
```

![figure1](https://github.com/gahaalt/slicemap/blob/main/figures/figure1.png?raw=true)

#### Include `start` | `end`

```
from slicemap import SliceMap
sm1 = SliceMap(inlcude="start")
sm1[2:3] = 1
sm1[3:4] = 2
sm1[4:5] = 3
print(sm1[3], sm1[4])

sm2 = SliceMap(inlcude="end")
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
```

Outputs:

```
{(-inf,1): 0, [1,3): 11, [3,9): 13, [9,12): 0, [12,16): 7, [16,19): 3, [19,22): 18, [22,23): 3, [23,29): 13, [29,inf): 0}
[(-inf, 1, 0), (1, 3, 11), (3, 9, 13), (9, 12, 0), (12, 16, 7), (16, 19, 3), (19, 22, 18), (22, 23, 3), (23, 29, 13), (29, inf, 0)]
```

Depending on the exact task formulation, answer should be easy to retrieve from the above.
