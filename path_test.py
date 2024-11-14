import sys
import pathlib
sys.dont_write_bytecode = True
sys.path.append(pathlib.Path(__file__).parent.resolve())

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
