#!/bin/bash

# Set PYTHONPATH to the src directory so pytest can find the whywhytools package
export PYTHONPATH="src"

# Run pytest on the tests directory, passing any additional arguments
python -m pytest tests/ "$@"
