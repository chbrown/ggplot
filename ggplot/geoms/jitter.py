from copy import deepcopy
import numpy as np
from .base import geom_base


class geom_jitter(geom_base):
    VALID_AES = ['jitter']

    def __radd__(self, gg):
        gg = deepcopy(gg)
        xcol = gg.aesthetics.get("x")
        ycol = gg.aesthetics.get("y")
        x = gg.data[xcol]
        y = gg.data[ycol]
        x = x * np.random.uniform(.9, 1.1, len(x))
        y = y * np.random.uniform(.9, 1.1, len(y))
        gg.data[xcol] = x
        gg.data[ycol] = y
        return gg

    def plot_layer(self, layer):
        pass
