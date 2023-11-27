#!/bin/bash

# Check if PYCODE is set
if [ -z "$PYCODE" ]; then
    echo "Error: PYCODE environment variable not set."
    exit 1
fi

# Run the Python code
python3 -c "$PYCODE"

