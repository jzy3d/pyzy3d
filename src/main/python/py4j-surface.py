from py4j.java_gateway import JavaGateway
import numpy as np
import array as array
gateway = JavaGateway()

chart = gateway.entry_point.getChart()
#gateway.entry_point.open("test", 800, 600)



def create_java_object(gateway, numpy_matrix):
   print(numpy_matrix)
   print(numpy_matrix.shape)
   print(numpy_matrix.flatten().tolist())
   header = array.array('i', list(numpy_matrix.shape))

   listi = numpy_matrix.flatten().tolist()
   print(listi)

   body = array.array('i', listi);
   if sys.byteorder != 'big':
      header.byteswap()
      body.byteswap()
   buf = bytearray(header.tostring() + body.tostring())
   return gateway.entry_point.createFromPy4j(buf)



a = np.matrix('1 2 3 4')
print(a[0])


#b = create_java_object(gateway, a)
#print(b)

import random

size = 100
c = gateway.jvm.org.jzy3d.maths.Coord3ds(size)
ratio  =1000
for i in range(0,size):
    x = random.random() * ratio
    y = random.random() * ratio
    z = random.random() * ratio

    r = 1.0#random.random()
    g = 0.0#random.random()
    b = 0.0#random.random()
    a = 1.0
    c.set(i, x, y, z, r, g, b, a)

scatter = gateway.entry_point.scatter(c)
print(c.toString())
gateway.entry_point.console(c)

#chart.add(scatter)
chart.getScene().add(scatter)
gateway.entry_point.open("Pzy3d - Py4j", 800, 600)
