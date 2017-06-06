from py4j.java_gateway import JavaGateway
import time

'''
Chart controller.
'''
class Pyzy3d(object):
    '''
    Start and connect to a Pyzy3d Java Gateway.

    Might join an already started Pyzy3d Java Gateway (call Pyzy3d(False)).
    '''
    def __init__(self, startGateway=True, pzyJar = 'bin/pyzy3d-1.0.1-SNAPSHOT.jar'):
        # TRYING connecting on gateway
        #try:
        #self.gateway_client = self.gateway_connect()
        #except Exception:
        #  pass


        # Start gateway
        if startGateway:#self.gateway_client.is_connected is False:#startGateway:
            self.gateway_process = self.gateway_start(pzyJar)
            sleepTime = 5
            time.sleep(sleepTime)

        # Connect gateway
        self.gateway_client = self.gateway_connect()

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



    def gateway_start(self, pzyJar = 'bin/pyzy3d-1.0.1-SNAPSHOT.jar', showJavaOut = False):



        pid = 0

        import subprocess as sub
        print("Will start Pyzy3d Gateway : " + pzyJar)
        pid = sub.Popen(['java', '-jar', pzyJar], stdout=sub.PIPE,stderr=sub.PIPE)
        print("Pyzy3d gateway invoked : " + pzyJar)

        if showJavaOut:
            output, errors = p.communicate()
            print(output)
        return pid


    def gateway_connect(self):
        print("Joining Pyzy3d gateway ...")
        gateway = JavaGateway()
        print("Pyzy3d gateway joined")
        return gateway
