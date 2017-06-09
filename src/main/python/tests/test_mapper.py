import pyzy3d.func3d as f3d
import pytest

func = f3d.Func3d(monitor=True)

z1 = func.f(1,1)

print(z1)

assert z1 == 1.3817732906760363
