# Pzy3d - 3d charts for Python

Build [Jzy3d](http://www.jzy3d.org) chart from Python

## Using Jython

### Install Jython

Mac OS
```
brew install jython
```

Other
```
google download jython
```

### Run example plots

```
./run-jython-scatter.sh
./run-jython-surface.sh
```

### Building Jzy3d Uber Jar for Python

Run ```mvn package``` and then use target/pzy3d-api-${version}.jar

You might wish to copy to ```bin``` to later call ```java -jar pzy3d-api-1.0.1-SNAPSHOT.jar``` to start Py4j gateway
