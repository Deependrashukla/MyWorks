#!/bin/bash

className="readDirectory"
path="/home/deependra/Documents/ajava/txtFiles"

echo "my java file class name is : $className"
echo "path of txt files is : $path"

javac $className.java
java $className $path
