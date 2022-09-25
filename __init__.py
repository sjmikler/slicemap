from .source.slicemap import SliceMap

try:
    import matplotlib.pyplot as plt

    from .source.plotting import plot_slicemap
except ImportError:
    pass
