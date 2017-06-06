from pyzy3d import Pyzy3d
from mapper import Mapper
import time


# A Pyzy instance
pz = Pyzy3d(startGateway=True, pzyJar="/Users/martin/dev/jzy3d/public/pyzy3d/target/pyzy3d-1.0.1-SNAPSHOT.jar")


func = Mapper()
surface = pz.new_surface(func, -3.0, 3.0, -3.0, 3.0, 10)

# Chart
chart = pz.chart(0)
chart.getQuality().setSmoothPoint(True)
chart.add(surface)
chart.open("Pyzy3d - Surface", 800, 600)

time.sleep(5)
chart.render()

pz.shutdown()
