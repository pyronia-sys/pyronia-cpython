#!/bin/bash

# This script builds a Pyronia-aware version of cpython, which can be
# installed on the system side-by-side vanilla Python.
# author: Marcela S. Melara

mkdir pyronia_build
cd pyronia_build

../configure --with-libs='-lnl-3 -lnl-genl-3 -lsmv -lpyronia'
make
