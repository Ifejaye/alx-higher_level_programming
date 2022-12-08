#!/usr/bin/python3
from sys import argv
if len(argv) == 1:
    print("{} argument:\n".format(len(argv)))
elif len(argv) == 0:
    print("{} argument.\n".format(len(argv)))
else:
     print("{} arguments:\n".format(len(argv)))
if len(argv) > 0:
    for arg in len(argv):
        print("{}: {}".format(arg, argv[arg]))