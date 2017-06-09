from pyzy3d.pyzy3d import Pyzy3d
from pyzy3d.generator import Generator

# A Pyzy instance
pz = Pyzy3d()#False, 'target/pyzy3d-1.0.1-SNAPSHOT.jar')

# Generate data
n = 30000
coords = pz.new_coords(n)
Generator().scatter(coords, n)


# Drawable scatter
scatter = pz.new_scatter(coords)
scatter.setWidth(5.0)


# Chart
chart = pz.chart(1)
chart.getQuality().setSmoothPoint(True);
chart.add(scatter)
chart.open("Pyzy3d - Scatter", 800, 600)


pz.shutdown()
