from pyzy3d.pyzy3d import Pyzy3d
from pyzy3d.generator import Generator
import pytest

pz = Pyzy3d()#True, 'target/pyzy3d-1.0.1-SNAPSHOT.jar')


assert pz.colormap("none") == None # verify non existing objects are returned as none

assert pz.new_coord(1.0,2.0,3.0) != None
print(pz.new_coord(1.0,2.0,3.0)) # console proof

assert pz.new_color(1.0,0.5,0.0,1.0) != None
assert pz.new_point() != None
assert pz.new_linestrip() != None
assert pz.new_polygon() != None
assert pz.new_quad() != None
assert pz.colormap("rainbow") != None
assert pz.colormap("hot") != None
assert pz.colormap("grayscale") != None
assert pz.colormap("rgb") != None

pz.shutdown()
