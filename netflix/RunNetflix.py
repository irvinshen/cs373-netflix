#!/usr/bin/env python3

# ------------------------------
# projects/netflix/RunNetflix.py
# taken from: projects/collatz/RunCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To run the program
    % python RunNetflix.py < RunNetflix.in > RunNetflix.out
    % chmod ugo+x RunNetflix.py
    % RunNetflix.py < RunNetflix.in > RunNetflix.out

To document the program
    % pydoc -w Netflix
"""

# -------
# imports
# -------

import sys

from Netflix import netflix_solve

# ----
# main
# ----

netflix_solve(sys.stdin, sys.stdout)
