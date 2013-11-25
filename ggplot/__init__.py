# For testing purposes we might need to set mpl backend before any
# other import of matplotlib.
def _set_mpl_backend():
    import os
    import matplotlib as mpl

    env_backend = os.environ.get('MATPLOTLIB_BACKEND')
    if env_backend:
        # we were instructed
        mpl.use(env_backend)

_set_mpl_backend()

# general
from .ggplot import *
from .exampledata import *

# geoms
from .geoms.abline import geom_abline
from .geoms.area import geom_area
from .geoms.bar import geom_bar
from .geoms.density import geom_density
from .geoms.histogram import geom_histogram
from .geoms.hline import geom_hline
from .geoms.jitter import geom_jitter
from .geoms.line import geom_line
from .geoms.point import geom_point
from .geoms.step import geom_step
from .geoms.tile import geom_tile
from .geoms.vline import geom_vline
