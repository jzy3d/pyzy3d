from java.util import Random
from org.jzy3d.chart.factories import AWTChartComponentFactory;
from org.jzy3d.colors import Color;
from org.jzy3d.maths import Coord3d;
from org.jzy3d.plot3d.primitives import Scatter;
from org.jzy3d.plot3d.rendering.canvas import Quality;

from jarray import zeros, array

# Generate scatter data
size = 500000;
points = array([Coord3d(0,0,0)] * size, Coord3d)
colors = array([Color(0,0,0)] * size, Color)
r = Random()
r.setSeed(0)
for i in range(0, size):
    x = r.nextFloat() - 0.5
    y = r.nextFloat() - 0.5
    z = r.nextFloat() - 0.5
    points[i] = Coord3d(x, y, z)
    colors[i] = Color(x, y, z, 0.25)

# Create scatter chart
scatter = Scatter(points, colors)
chart = AWTChartComponentFactory.chart(Quality.Advanced, "newt")
chart.getScene().add(scatter)
chart.addMouseCameraController()
chart.open("Pzy3d - Jython - Scatter", 800,600)
chart.render()
