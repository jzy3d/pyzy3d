

class Mapper(object):
    def f(self, x, y):
        return x+y

    class Java:
        implements = ['org.pyzy3d.PyFunc3d']
