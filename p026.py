import sys, os

print(os.stat(sys.argv[1]).st_size)