[![PyPI version](https://badge.fury.io/py/slicemap.svg)](https://badge.fury.io/py/slicemap)
[![Python 3.7](https://github.com/gahaalt/slicemap/actions/workflows/python37.yaml/badge.svg)](https://github.com/gahaalt/slicemap/actions/workflows/python37.yaml)
[![Python 3.8](https://github.com/gahaalt/slicemap/actions/workflows/python38.yaml/badge.svg)](https://github.com/gahaalt/slicemap/actions/workflows/python38.yaml)
[![Python 3.9](https://github.com/gahaalt/slicemap/actions/workflows/python39.yaml/badge.svg)](https://github.com/gahaalt/slicemap/actions/workflows/python39.yaml)
[![Python 3.10](https://github.com/gahaalt/slicemap/actions/workflows/python310.yml/badge.svg)](https://github.com/gahaalt/slicemap/actions/workflows/python310.yml)

Slicemap is a tiny package introducing a useful, dictionary-like data structure,
similar to a normal Python dict, but instead of setting values key by key, you set entire slices at once.

It is a useful data structure implemented entirely in Python with help of `sortedcontainers` package.
Initially, I used a custom skip-list implementation, but this wasn't as fast as `sortedcontainers`
([see their benchmarks](https://grantjenks.com/docs/sortedcontainers/performance-scale.html)).

Adding new slices and querying values both have `O(log(n))` time complexity.
Adding new slices might make old ones become redundant.
Thus `n` correspondes to the maximal number of slices present in SliceMap at a time.

Install easily with pip:

```
pip install slicemap
```

* [See Documentation](https://gahaalt.github.io/slicemap/)
* [See on GitHub](https://github.com/gahaalt/slicemap)
* [See on PyPI](https://pypi.org/project/slicemap/)

