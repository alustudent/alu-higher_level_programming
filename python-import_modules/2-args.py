#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    if count == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(count, "" if count == 1 else "s"))
        for i in range(1, count + 1):
            print("{}: {}".format(i, argv[i]))
