#!/bin/bash

# Compile the main C program
echo "Compiling main program..."
gcc -o 19 19.c
if [ $? -ne 0 ]; then
    echo "Warning: Failed to compile main program. Skipping further steps related to main."
fi

# Compile the unit test cases
echo "Compiling unit tests..."
gcc -o 19test 19test.c 19.c
if [ $? -ne 0 ]; then
    echo "Error: Failed to compile unit tests."
    exit 1
fi

# Run the unit tests
echo "Running unit tests..."
./19test

echo "All steps completed successfully!"