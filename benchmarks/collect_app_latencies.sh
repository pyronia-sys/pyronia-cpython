#!/bin/bash

# Run 10 trials for a given application, and collect the end-to-end latency for  each run

runs=25

app=$1

for (( x=0; x<=$runs; x++)) 
do
    ../load_python_profile
    ../pyronia_build/python $app
    echo "Finished run $x "
done
