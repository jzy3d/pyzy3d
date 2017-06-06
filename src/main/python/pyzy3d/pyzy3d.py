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
        self.gateway_client = self.gateway_connect()

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
    Instanciate a Java Coord3ds that can be populated from Python.
    '''
    def new_coords(self, size):
        return self.gateway_client.jvm.org.jzy3d.maths.Coord3ds(size)

    def new_scatter(self, coords):
        return self.gateway_client.entry_point.newScatter(coords)

    def new_surface(self, mapper, xmin=-1.0, xmax=+1.0, ymin=-1.0, ymax=+1.0, steps=100):
        return self.gateway_client.entry_point.newSurface(mapper, xmin, xmax, ymin, ymax, steps)


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

    def gateway_connect(self):
        print("Joining Pyzy3d gateway ...")
        gateway = JavaGateway(start_callback_server=True)
        gateway.restart_callback_server()
        print("Pyzy3d gateway joined")
        return gateway
