# Script Name       : fileinfo.py
# Author                : Not sure where I got this from
# Created               : 28th November 2011
# Last Modified     :
# Version               : 1.0
# Modifications     :

# Description           : Show file information for a given file


# get file information using os.stat()
# tested with Python24 vegsaeat 25sep2006
from __future__ import print_function

import os
import stat  # index constants for os.stat()
import sys
import time
