import sys
import importlib

module = importlib.import_module(sys.argv[2])
run = getattr(module, sys.argv[1])
run()