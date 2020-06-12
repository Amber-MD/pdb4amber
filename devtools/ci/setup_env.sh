#!/bin/sh

if [ "$TRAVIS_OS_NAME" = "osx" ]; then
    wget http://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O miniconda.sh;
else
    wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh;
fi

bash miniconda.sh -b

export PATH=$HOME/miniconda3/bin:$PATH
# install stable version

# create myenv
conda create -y -n myenv python=$PYTHON_VERSION 

# switch env
source activate myenv
conda install numpy nomkl -y
conda install scipy -y
conda install coverage -y 
# conda install libgfortran -c conda-forge -y

conda install ambertools -c conda-forge -y
pip install mock

# pytest
pip install pytest
pip install pytest-cov

# coveralls
pip install coveralls
