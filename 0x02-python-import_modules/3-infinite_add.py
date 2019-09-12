#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    for x in range(1, len(sys.argv)):
        add = add + int(sys.argv[x])
    print("{:d}".format (add))
