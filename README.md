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

### Building Jzy3d Uber Jar for Jython

To ease classpath definition, we bundle Jzy3d and its dependencies in a single jar file (bin/jzy3d-api-1.0.1-SNAPSHOT.jar).
To build this Jar we add to the API [pom file](https://github.com/jzy3d/jzy3d-api/blob/master/jzy3d-api/pom.xml)
the Maven Shade plugin and then invoke ```mvn package```:
```
 <build>
   <plugins>
    ...
    <plugin>
      	<groupId>org.apache.maven.plugins</groupId>
      	<artifactId>maven-shade-plugin</artifactId>
      	<version>2.4.3</version>
      	<executions>
      		<execution>
      			<phase>package</phase>
      			<goals>
      				<goal>shade</goal>
      			</goals>
      			<configuration>
      				<filters>
      					<filter>
      						<artifact>*:*</artifact>
      						<excludes>
      							<exclude>META-INF/*.SF</exclude>
      							<exclude>META-INF/*.DSA</exclude>
      							<exclude>META-INF/*.RSA</exclude>
      						</excludes>
      					</filter>
      				</filters>

      				<artifactSet>
      					<excludes>
      						<exclude>classworlds:classworlds</exclude>
      						<exclude>jmock:*</exclude>
      						<exclude>*:xml-apis</exclude>
      						<exclude>org.apache.maven:lib:tests</exclude>
      					</excludes>
      				</artifactSet>
      				<transformers>
      					<transformer
      						implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
      					</transformer>
      				</transformers>
      			</configuration>
      		</execution>
      	</executions>
      </plugin>
     ...
     </plugins>
    </build>
```
