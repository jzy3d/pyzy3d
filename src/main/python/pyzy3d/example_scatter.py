from pyzy3d import Pyzy3d
from generator import Generator

# A Pyzy instance
pz = Pyzy3d()#True, 'target/pyzy3d-1.0.1-SNAPSHOT.jar')

# Generate data
n = 10000
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
