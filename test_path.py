import sys
sys.dont_write_bytecode = True

import os
import subprocess
import json
import ctypes

import threading
from settings import *

focus_roblox()
print("started")
exec(open("paths.py"))
print("finished")
