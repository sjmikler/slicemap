[![PyPi version](https://badgen.net/pypi/v/slicemap)](https://pypi.org/project/slicemap/)
[![PyPI license](https://img.shields.io/pypi/l/slicemap)](https://pypi.org/project/slicemap/)
[![Python 3.7](https://github.com/gahaalt/slicemap/actions/workflows/python37.yaml/badge.svg)](https://github.com/gahaalt/slicemap/actions/workflows/python37.yaml)
[![Python 3.8](https://github.com/gahaalt/slicemap/actions/workflows/python38.yaml/badge.svg)](https://github.com/gahaalt/slicemap/actions/workflows/python38.yaml)
[![Python 3.9](https://github.com/gahaalt/slicemap/actions/workflows/python39.yaml/badge.svg)](https://github.com/gahaalt/slicemap/actions/workflows/python39.yaml)
[![Python 3.10](https://github.com/gahaalt/slicemap/actions/workflows/python310.yml/badge.svg)](https://github.com/gahaalt/slicemap/actions/workflows/python310.yml)

Package slicemap is introducing a useful, dictionary-like data structure,
similar to normal Python dict, but instead of setting values key by key, you set entire slices.

* Implemented entirely in Python
* Has only one dependency: [sortedcontainers](https://grantjenks.com/docs/sortedcontainers/)
* It is efficient, it has `O(log(n))` time complexity for insertion and query
    * Adding new slices might make old ones become redundant.
      Thus `n` correspondes to the maximal number of slices present in SliceMap at a time
* Makes life easier, see [applications](https://gahaalt.github.io/slicemap/applications/)

## Installation

Install easily with pip:

```
pip install slicemap
```

Or download from source and install locally:

```
git clone https://github.com/gahaalt/slicemap.git
cd slicemap && pip install -e .
```

## Links

* [See Documentation](https://gahaalt.github.io/slicemap/)
* [See on GitHub](https://github.com/gahaalt/slicemap)
* [See on PyPI](https://pypi.org/project/slicemap/)

