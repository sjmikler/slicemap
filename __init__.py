from .source.slicemap import SliceMap

try:
    from .source.plotting import plot_slicemap
except ImportError:
    pass
