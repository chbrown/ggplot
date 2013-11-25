import matplotlib.pyplot as plt
from copy import deepcopy
import pandas as pd
from .base import geom_base


class stat_bin2d(geom_base):
    VALID_AES = ['x', 'y', 'alpha', 'label']

    def plot_layer(self, layer):
        layer = {k: v for k, v in layer.items() if k in self.VALID_AES}
        layer.update(self.manual_aes)

        x = layer.pop('x')
        y = layer.pop('y')

        plt.hist2d(x, y, cmap=plt.cm.Blues, **layer)
