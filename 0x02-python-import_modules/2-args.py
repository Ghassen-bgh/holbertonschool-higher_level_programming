#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    e = sys.argv
    size = len(e) - 1
    ar = "argument" if size is 1 else "arguments"
    dot = "." if size is 0 else ":"
    print("{} {}".format(size, ar + dot))
    for i in range(1, size + 1):
        print("{}: {}".format(i, e[i]))
