from matplotlib import pyplot as plt
import tikzplotlib
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable


RC_PARAMS = {"figure.figsize": [5, 5], "figure.dpi": 220, "pgf.rcfonts": False}


with plt.rc_context(rc=RC_PARAMS):
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.fill_between(
        np.arange(3), 0, 1
    )  # when using logscale, filling between 0 and something else does not work
    ax.fill_between(np.arange(3), 1, 10)

    ax.set_title("Doesn't Work")
    ax.set_yscale("log")
    tikzplotlib.save("test1.tikz")


plt.close()

with plt.rc_context(rc=RC_PARAMS):
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.fill_between(
        np.arange(3), 1.0e-6, 1
    )  # however, it works to just use an arbitrarily small number
    ax.fill_between(np.arange(3), 1, 10)

    ax.set_title("Works")
    ax.set_yscale("log")
    tikzplotlib.save("test2.tikz")

