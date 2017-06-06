# Pzy3d - 3d charts for Python

Build [Jzy3d](http://www.jzy3d.org) charts for Python.

Jzy3d is a java library, hence calling it from Python might be done by several manners :
* Py4j binding : python initialize a Java Virtual Machine acting like a server. Python scripts then exchange informations with this server. See ```src/main/python/py4j-*.py```
* Jython : your python program is interpreted inside a JVM. Your program can use Java objects. See ```src/main/jython/jython-*.py```

## Using Py4j

Py4j allows calling a Java Virtual Machine from Python. Py4j can call java methods and access java instance references.

### Install Py4j

Update python
```
pip install py4j
```

### Run example plots

```
./run-py4j-query-scatter.sh
```

Will:
* Start a JVM using Pzy3d Jar file located in bin/
* Initialize a java [Coord3ds](https://github.com/jzy3d/jzy3d-api/blob/master/jzy3d-api/src/api/org/jzy3d/maths/Coord3ds.java) to provide a java point cloud Reference
* Set coordinates and colors from python
* Open a Jzy3d chart


## Using Jython

### Install Jython

* Mac OS ```brew install jython```
* Other ```google install jython```


## Run example plots

```
./run-jython-scatter.sh
./run-jython-surface.sh
```

## (Re)Building Pzy3d Jar for Jython and Py4j

Compile as follow
```
mvn clean package
```

Update current Pzy3d binary
```
cp target/pzy3d-api-1.0.1-SNAPSHOT.jar bin/
```

### Using Pzy3d with Py4j
Py4j requires gateway to be started with ```java -jar bin/pzy3d-api-1.0.1-SNAPSHOT.jar```. Then run a script like ```python src/main/python/py4j-scatter.py```

### Using Pzy3d with Jython
Jython requires path to be defined as follow ```jython -Dpython.path=bin/pzy3d-api-1.0.1-SNAPSHOT.jar src/main/jython/jython-surface.py```


## Note for Python distrib

* https://python-packaging.readthedocs.io/en/latest/
* https://github.com/urbanairship/mvn-python-packaging/blob/master/pom.xml
