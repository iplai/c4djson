"""
Author: Dale Chan
Name-en-US: Dump Document
Description-en-US: Dump and print json from doc with selected active object (in hierarchy) and selected meterials
"""
from c4djson.core import *

if __name__ == "__main__":
    print(Dict2Str(DumpSelected()))
