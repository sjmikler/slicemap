import matplotlib.pyplot as plt


def plot_slicemap(slicemap, show=True):
    """Plot SliceMap.

    Parameters
    ----------
    slicemap
        The SliceMap to be plotted.
    show
        If True, `plt.show()` will be called after creating the figure.

    Returns
    -------
    None
    """
    plt.figure(constrained_layout=True)

    ticks = [x.up_to_key for x in slicemap.data if abs(x.up_to_key) < float("inf")]
    mind = ticks[0]
    maxd = ticks[-1]
    span = maxd - mind
    mind -= span / 5
    maxd += span / 5

    granularity = (maxd - mind) / 1000

    xs = []
    ys = []

    x = mind
    while x < maxd:
        try:
            # In case if raise_key_error is True
            y = slicemap.__getitem__(x)
        except KeyError:
            y = None

        if y is not None:
            xs.append(x)
            ys.append(y)
        elif xs:
            plt.plot(xs, ys)
            xs = []
            ys = []
        x += granularity

    if xs:
        plt.plot(xs, ys)

    plt.grid(alpha=0.5)
    plt.xlabel("Keys")
    plt.ylabel("Values")
    if show:
        plt.show()
