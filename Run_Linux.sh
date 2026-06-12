#!/bin/bash

cd "$(dirname "$0")"

python setup.py

source env/bin/activate

python main.py

deactivate
