#%%

import numpy as np
import matplotlib as plt
from einsteinpy.geodesic import Timelike
from einsteinpy.geodesic import Nulllike
from einsteinpy.plotting.geodesic import StaticGeodesicPlotter
from einsteinpy.hypersurface import SchwarzschildEmbedding
from einsteinpy.plotting import HypersurfacePlotter
from astropy import units as u
from matplotlib import animation
from matplotlib.animation import FuncAnimation, PillowWriter 
from PIL import Image


#----- Running in a normal python file as animations weren't working on notebook (vscode) -----
# also user may need to rotate the 3d viewer to see the graph better


# Positions given by r, theta, phi
position = np.array([30., np.pi / 4, 0])
momentum = np.array([0.0, 0, 3.0]) 

# Spin is 0 since Schwarzchild black holes do not rotate
a = 0

# Solver steps (length of simumlation)
steps = 2000

# Step size
delta = 1

geod1 = Timelike(
    metric="Schwarzschild",
    metric_params=(a,),
    position=position,
    momentum=momentum,
    steps=steps,
    delta=delta,
    return_cartesian=True
)

sgpl = StaticGeodesicPlotter()
#sgpl.plot(geod1)
sgpl.animate(geod1, interval=2)

#sgpl.ani.save('animation.gif', fps=60)
sgpl.show()

#sgpl2 = StaticGeodesicPlotter()
#sgpl2.plot2D(geod1, coordinates=(1, 2))