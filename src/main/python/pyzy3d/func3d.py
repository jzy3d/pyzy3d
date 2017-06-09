from numpy import *

class Func3d(object):
    def __init__(self, monitor=False):
        self.k = 0
        self.doMonitor = monitor

    def f(self, x, y):
        self.monitor()
        #return x-0.5 * y
        return cos(x) + sin(y)

    def monitor(self):
        if self.doMonitor:
            if (self.k % 10) == 0:
                print(self.k)
            self.k = self.k+1

    class Java:
        implements = ['org.pyzy3d.PyFunc3d']
