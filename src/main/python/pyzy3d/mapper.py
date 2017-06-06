class Mapper(object):
    def __init__(self):
        self.k = 0
        self.monitor = False
    def f(self, x, y):
        if self.monitor:
            if (self.k % 10) == 0:
                print(self.k)
            self.k = self.k+1
        return x+y

    class Java:
        implements = ['org.pyzy3d.PyFunc3d']
