from pyzy3d.pyzy3d import Pyzy3d
import pyzy3d
import time
import numpy as np

# A Pyzy instance
pz = Pyzy3d(startGateway=True, pzyJar="/Users/martin/dev/jzy3d/public/pyzy3d/target/pyzy3d-1.0.1-SNAPSHOT.jar")


func = Mapper(monitor=True)
surface = pz.new_surface(func, -2 * np.pi, 2 * np.pi, -2 * np.pi, 2 * np.pi, 50)

# Chart
chart = pz.chart(0)
chart.getQuality().setSmoothPoint(True)
chart.add(surface)
chart.open("Pyzy3d - Surface", 800, 600)
time.sleep(5)
chart.render()

pz.shutdown()
