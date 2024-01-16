# Applications

## [The Skyline Problem](https://www.geeksforgeeks.org/the-skyline-problem-set-2/)

Easily solvable in `O(n*log(n))` time:

```py
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
{[-inf,1): 0, [1,3): 11, [3,9): 13, [9,12): 0, [12,16): 7, [16,19): 3, [19,22): 18, [22,23): 3, [23,29): 13, [29,inf]: 0}
[(-inf, 1, 0), (1, 3, 11), (3, 9, 13), (9, 12, 0), (12, 16, 7), (16, 19, 3), (19, 22, 18), (22, 23, 3), (23, 29, 13), (29, inf, 0)]
```

You can also use plotting utility:
```
sm.plot()
```
![figure2](https://github.com/gahaalt/slicemap/blob/main/docs/figures/figure2.png?raw=true)

Depending on the exact task formulation, answer should be easy to retrieve from the above.
