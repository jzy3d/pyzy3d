from pyzy3d.pyzy3d import Pyzy3d
from pyzy3d.generator import Generator
import pytest

pz = Pyzy3d(True)
assert pz.new_coord(1.0,2.0,3.0) != None
pz.shutdown()


pz = Pyzy3d(False)
assert pz.new_coord(1.0,2.0,3.0) != None
pz.shutdown()
