from pyzy3d import Pyzy3d
from generator import Generator

# A Pyzy instance
pz = Pyzy3d()#True, 'target/pyzy3d-1.0.1-SNAPSHOT.jar')

print(pz.new_coord(1.0,2.0,3.0))
print(pz.new_color(1.0,0.5,0.0,1.0))
print(pz.new_point())
print(pz.new_linestrip())
print(pz.new_polygon())
print(pz.new_quad())
print(pz.colormap("rainbow"))
print(pz.colormap("hot"))
print(pz.colormap("grayscale"))
print(pz.colormap("rgb"))
print(pz.colormap("none"))

pz.shutdown()
