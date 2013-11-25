import matplotlib.pyplot as plt
from pandas.lib import Timestamp
import numpy as np
from .base import geom_base


class geom_abline(geom_base):
    VALID_AES = ['x', 'slope', 'intercept', 'color', 'linestyle', 'alpha', 'label']

    def plot_layer(self, layer):
        layer = {k: v for k, v in layer.items() if k in self.VALID_AES}
        layer.update(self.manual_aes)
        if 'x' in layer:
            x = layer.pop('x')
        if 'slope' in layer:
            slope = layer.pop('slope')
        else:
            slope = 1.0
        if 'intercept' in layer:
            intercept = layer.pop('intercept')
        else:
            intercept = 0.0
        if isinstance(x[0], Timestamp):
            gca = plt.gca()
            gca.set_autoscale_on(False)
            gca.plot(gca.get_xlim(), gca.get_ylim())
        else:
            start, stop = np.max(x), np.min(x)
            step = ((stop-start)) / 100.0
            x_rng = np.arange(start, stop, step)
            y_rng = x_rng * slope + intercept
            plt.plot(x_rng, y_rng, **layer)
