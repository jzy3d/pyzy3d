from pyzy3d import Pyzy3d
from generator import Generator
from mapper import Mapper

# A Pyzy instance
pz = Pyzy3d()#True, 'target/pyzy3d-1.0.1-SNAPSHOT.jar')


func = Mapper()
surface = pz.new_surface(func, -3.0, 3.0, -3.0, 3.0, 80)

# Chart
chart = pz.chart(0)
chart.getQuality().setSmoothPoint(True);
chart.add(surface)
chart.open("Pyzy3d - Scatter", 800, 600)
