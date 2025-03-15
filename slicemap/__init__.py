__license__ = "MIT"
__version__ = "1.2.0"
__author__ = "Szymon Mikler"

from .slicemap import SliceMap

try:
    from .plotting import plot_slicemap
except ImportError:
    pass
