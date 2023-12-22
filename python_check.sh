#!/bin/bash
if [[ -x "$(command -v python3)" ]] 
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv != "Python 3"* ]] 
    then
        echo "Python 3.9.x or higher is recommended for running this program." >&2
    else
        echo "You have Python 3 installed. To continue, please run 'run.sh." >&2
    fi 
else
    echo "This program requires Python 3 to be installed.
    Please install Python at https://www.python.org/downloads/" >&2
fi