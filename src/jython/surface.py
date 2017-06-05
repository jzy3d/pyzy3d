from org.jzy3d.analysis import AbstractAnalysis
from org.jzy3d.analysis import AnalysisLauncher
from org.jzy3d.chart.factories import AWTChartComponentFactory
from org.jzy3d.colors import Color
from org.jzy3d.colors import ColorMapper
from org.jzy3d.colors.colormaps import ColorMapRainbow
from org.jzy3d.maths import Range
from org.jzy3d.plot3d.builder import Builder
from org.jzy3d.plot3d.builder import Mapper
from org.jzy3d.plot3d.builder.concrete import OrthonormalGrid
from org.jzy3d.plot3d.primitives import Shape
from org.jzy3d.plot3d.rendering.canvas import Quality
from java.lang import Math


# Define a function to plot
class Function3d(Mapper):
    def __init__(self):
        return
    def f(self, x, y):
        return x * Math.sin(x * y)
mapper = Function3d()


# Define range and precision for the function to plot
range = Range(-3, 3)
steps = 80

# Create the object to represent the function over the given range.
surface = Builder.buildOrthonormal(OrthonormalGrid(range, steps, range, steps), mapper)
surface.setColorMapper(ColorMapper(ColorMapRainbow(), surface.getBounds().getZmin(), surface.getBounds().getZmax(), Color(1, 1, 1, .5)))
surface.setFaceDisplayed(True)
surface.setWireframeDisplayed(False)

# Create a chart
chart = AWTChartComponentFactory.chart(Quality.Advanced, "awt")
chart.getScene().getGraph().add(surface)
chart.open("Pzy3d - surface", 800, 600)
chart.render()
