# Python Slice Map

[//]: # (To get badges go to https://shields.io/ and use https://pypi.org/pypi/slicemap/json as data url. Query fields using dot as the separator.)

[![PyPi version](https://img.shields.io/badge/dynamic/json?label=latest&query=info.version&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fslicemap%2Fjson)](https://pypi.org/project/slicemap)
[![PyPI license](https://img.shields.io/badge/dynamic/json?label=license&query=info.license&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fslicemap%2Fjson)](https://pypi.org/project/slicemap/)
[![Documentation Status](https://readthedocs.org/projects/slicemap/badge/?version=latest)](https://slicemap.readthedocs.io/en/latest/?badge=latest)
[![Python 3.7](https://github.com/gahaalt/slicemap/actions/workflows/python37.yaml/badge.svg)](https://github.com/gahaalt/slicemap/actions/workflows/python37.yaml)
[![Python 3.8](https://github.com/gahaalt/slicemap/actions/workflows/python38.yaml/badge.svg)](https://github.com/gahaalt/slicemap/actions/workflows/python38.yaml)
[![Python 3.9](https://github.com/gahaalt/slicemap/actions/workflows/python39.yaml/badge.svg)](https://github.com/gahaalt/slicemap/actions/workflows/python39.yaml)
[![Python 3.10](https://github.com/gahaalt/slicemap/actions/workflows/python310.yaml/badge.svg)](https://github.com/gahaalt/slicemap/actions/workflows/python310.yaml)

Slicemap is a MIT licensed library introducing a useful, dictionary-like data structure,
similar to normal Python dict, but instead of setting values key by key, you set entire slices.

Features:

* Implemented entirely in Python
* Has only one dependency: [sortedcontainers](https://grantjenks.com/docs/sortedcontainers/)
* Is efficient, it has ``O(log(n))`` time complexity for insertion and query
    * Adding new slices might make old ones become redundant
    * ``n`` correspondes to the maximal number of slices present in SliceMap at a time
* Makes life easier, see [applications](https://slicemap.readthedocs.io/en/latest/applications/)

## Example

```py
>>> from slicemap import SliceMap
>>> sm = SliceMap()
>>> sm[-3:3] = 0.1
>>> sm[6.5:] = "Hello, SliceMap"
>>> sm[0]
0.1
>>> sm[10]
'Hello, SliceMap'
```

**See more examples in [Quick Start](https://slicemap.readthedocs.io/en/latest/quick_start/).**


## Installation

Install easily with pip:

```
pip install slicemap
```

## Links

* [Read Documentation](https://slicemap.readthedocs.io/)
* [See on GitHub](https://github.com/gahaalt/slicemap/)
* [See on PyPI](https://pypi.org/project/slicemap/)
