# Python Slice Map

[//]: # (To get badges go to https://shields.io/ and use https://pypi.org/pypi/slicemap/json as data url. Query fields using dot as the separator.)

[![PyPi version](https://img.shields.io/badge/dynamic/json?label=latest&query=info.version&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fslicemap%2Fjson)](https://pypi.org/project/slicemap)
[![PyPI license](https://img.shields.io/badge/dynamic/json?label=license&query=info.license&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fslicemap%2Fjson)](https://github.com/sjmikler/slicemap/blob/main/LICENSE.txt)

Slicemap is a MIT licensed library introducing a useful, dictionary-like data structure,
similar to normal Python dict, but instead of setting values key by key, you set entire slices.

Features:

* Implemented entirely in Python
* Has only one dependency: [sortedcontainers](https://grantjenks.com/docs/sortedcontainers/)
* Is efficient, it has ``O(log(n))`` time complexity for insertion and query
    * Adding new slices might make old ones become redundant
    * ``n`` correspondes to the maximal number of slices present in SliceMap at a time
* Makes life easier, see [applications](docs/applications.md)

## Example

```py
from slicemap import SliceMap
sm = SliceMap()
sm[-3:3] = 0.1
sm[6.5:] = "Hello, SliceMap"
print(sm[0])
print(sm[10])
```

```stdout
0.1
'Hello, SliceMap'
```

**See more examples in [Quick Start](docs/quick-start.md).**


## Installation

Install easily with pip:

```
pip install slicemap
```

## Links

* [Read Documentation](https://github.com/sjmikler/slicemap/tree/main/docs)
* [See on GitHub](https://github.com/gahaalt/slicemap/)
* [See on PyPI](https://pypi.org/project/slicemap/)
