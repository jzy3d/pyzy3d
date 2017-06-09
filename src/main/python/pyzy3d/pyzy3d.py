from py4j.java_gateway import JavaGateway
import time
import os

DEFAULT_JAR = os.path.dirname(os.path.abspath(__file__)) + '/bin/pyzy3d-1.0.1-SNAPSHOT.jar'

'''
Chart controller.
'''
class Pyzy3d(object):
    '''
    Start and connect to a Pyzy3d Java Gateway.

    Might join an already started Pyzy3d Java Gateway (call Pyzy3d(False)).

    You might have to kill the gateway process.
    '''
    def __init__(self, startGateway=True, pzyJar = DEFAULT_JAR):
        # TRYING connecting on gateway
        #test = None
        #try:
        #    self.gateway_client = self.gateway_connect()
        #    test = self.chart(0)
        #except Exception:
            #self.shutdown()
        #    pass

        #print(test)

        # Start gateway
        if startGateway:#test == None: ##self.gateway_client.is_connected is False:#startGateway:
            self.gateway_process = self.gateway_start(pzyJar)
            sleepTime = 4
            time.sleep(sleepTime)

        # Connect gateway
        self.gateway_client = self.gateway_connect(startGateway)

    def shutdown(self):
        self.gateway_client.shutdown_callback_server()
        self.gateway_client.shutdown()
    def shutdown_callback_server(self):
        self.gateway_client.shutdown_callback_server()

    '''
    Initialiaze or retrieve a chart identified by an integer ID.
    '''
    def chart(self, id=0):
        return self.gateway_client.entry_point.getOrCreateChart(id)

    '''
    Instanciate a Java Coord3ds that can be edited from Python.
    '''
    def new_coords(self, size=4):
        return self.gateway_client.jvm.org.jzy3d.maths.Coord3ds(size)

    '''
    Instanciate a Java Coord3d that can be edited from Python.
    '''
    def new_coord(self, x=0.0, y=0.0, z=0.0):
        return self.gateway_client.jvm.org.jzy3d.maths.Coord3d(x,y,z)

    '''
    Instanciate a Java Color that can be edited from Python.
    '''
    def new_color(self, r=0.0, g=0.0, b=0.0, a=1.0):
        return self.gateway_client.jvm.org.jzy3d.colors.Color(r, g, b, a)

    '''
    Instanciate a Java Point that can be edited from Python.
    '''
    def new_point(self):
        return self.gateway_client.jvm.org.jzy3d.plot3d.primitives.Point()

    '''
    Instanciate a Java LineStrip that can be edited from Python.
    '''
    def new_linestrip(self):
        return self.gateway_client.jvm.org.jzy3d.plot3d.primitives.LineStrip()

    '''
    Instanciate a Java Polygon that can be edited from Python.
    '''
    def new_polygon(self):
        return self.gateway_client.jvm.org.jzy3d.plot3d.primitives.Polygon()

    '''
    Instanciate a Java Quad that can be edited from Python.
    '''
    def new_quad(self):
        return self.gateway_client.jvm.org.jzy3d.plot3d.primitives.Quad()

    '''
    Instanciate a Java TesselatedPolygon that can be edited from Python.
    '''
    def new_polygon_tesselated(self, pointArray):
        return self.gateway_client.jvm.org.jzy3d.plot3d.primitives.TesselatedPolygon(pointArray)

    '''
    Instanciate a Java Scatter that can be edited from Python.
    '''
    def new_scatter(self, coords):
        return self.gateway_client.entry_point.newScatter(coords)

    '''
    Instanciate a Java Shape that can be edited from Python.
    '''
    def new_surface(self, mapper, xmin=-1.0, xmax=+1.0, ymin=-1.0, ymax=+1.0, steps=100):
        return self.gateway_client.entry_point.newSurface(mapper, xmin, xmax, ymin, ymax, steps)

    def colormap(self, name):
        if name == "rainbow":
            return self.gateway_client.jvm.org.jzy3d.colors.colormaps.ColorMapRainbow()
        elif name == "hot":
            return self.gateway_client.jvm.org.jzy3d.colors.colormaps.ColorMapHotCold()
        elif name == "grayscale":
            return self.gateway_client.jvm.org.jzy3d.colors.colormaps.ColorMapGrayscale()
        elif name == "rgb":
            return self.gateway_client.jvm.org.jzy3d.colors.colormaps.ColorMapRBG()
        else:
            return None

    def gateway_start(self, pzyJar = DEFAULT_JAR, showJavaOut = False):
        import subprocess as sub
        print("Will start Pyzy3d Gateway : " + pzyJar)
        pid = 0
        pid = sub.Popen(['java', '-jar', pzyJar], stdout=sub.PIPE,stderr=sub.PIPE)
        print("Pyzy3d gateway invoked : " + pzyJar)

        if showJavaOut:
            output, errors = p.communicate()
            print(output)
        return pid

    def gateway_connect(self, callback_server=True):
        print("Joining Pyzy3d gateway ...")
        gateway = JavaGateway(start_callback_server=callback_server)
        gateway.restart_callback_server()
        print("Pyzy3d gateway joined")
        return gateway
