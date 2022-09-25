[![PyPI version](https://badge.fury.io/py/slicemap.svg)](https://badge.fury.io/py/slicemap)

# Quick Start

```
from slicemap import SliceMap
sm = SliceMap()

sm[-10:10] = 0
sm[2:4] = 1
sm[4:6] = 2
sm[7:9] = 3
sm[12:15] = 1.5
sm.plot()
```

![figure1](https://raw.githubusercontent.com/gahaalt/slicemap/figures/figure1.png)
