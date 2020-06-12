#!/bin/sh

# change folder to avoid remove source code. ack.
(cd tests && rm -rf `python -c "import pdb4amber; import os; print(os.path.dirname(pdb4amber.__file__))"`)
pip install .
