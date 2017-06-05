import logging

#logging.setConsoleLevel(logging.ERROR)

# ############################################
# Start Pzy3d gateway

autoStart = True
showJavaOut = False
pzyJar = 'bin/pzy3d-api-1.0.1-SNAPSHOT.jar'
sleepTime = 5
pid = 0

if autoStart:
    import subprocess as sub
    print("Will start Pzy3d Gateway : " + pzyJar)
    pid = sub.Popen(['java', '-jar', pzyJar], stdout=sub.PIPE,stderr=sub.PIPE)
    print("Pzy3d gateway invoked : " + pzyJar)

    if showJavaOut:
        output, errors = p.communicate()
        print output
    else:
        import time
        time.sleep(sleepTime)

# ############################################
# Connect to Pzy3d gateway

from py4j.java_gateway import JavaGateway
print("Joining Pzy3d gateway ...")
gateway = JavaGateway()
print("Pzy3d gateway joined")

# ############################################
# Generate data

import random

size = 10000
coords = gateway.jvm.org.jzy3d.maths.Coord3ds(size)
ratio  =1000
for i in range(0,size):
    r = random.random()
    g = random.random()
    b = random.random()

    x = r * ratio
    y = g * ratio
    z = b * ratio

    a = 0.25
    coords.set(i, x, y, z, r, g, b, a)

# ############################################
# Create scatter
# gateway.entry_point.console(coords)
scatter = gateway.entry_point.scatter(coords)
scatter.setWidth(5.0)

# ############################################
# Configure and open chart
chart = gateway.entry_point.getChart()
chart.getQuality().setSmoothPoint(True)
gateway.entry_point.open("Pzy3d - Py4j - Scatter", 800, 600)


# ############################################
# Info

print("Pzy3d Gateway PID : ")
print(pid)
