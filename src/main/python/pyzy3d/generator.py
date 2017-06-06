import random



class Generator(object):

    def __init__(self):
        self.ratio = 1000
    def scatter(self, coords, size):
        for i in range(0,size):
            r = random.random()
            g = random.random()
            b = random.random()

            x = r * self.ratio
            y = g * self.ratio
            z = b * self.ratio

            a = 0.25

            coords.set(i, x, y, z, r, g, b, a)
