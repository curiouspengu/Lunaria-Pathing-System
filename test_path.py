import sys
sys.dont_write_bytecode = True
from settings import *

focus_roblox()
print("started")
exec(open("paths.py"))
print("finished")
