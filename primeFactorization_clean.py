#Aaron Guillen
#October 2016

def primeFactors(x):
    "This function returns a list of the prime factors of our parameter"
    ret = []

    if x < 0:
        ret.append(-1)
        x *= -1
    elif x == 0:
        ret.append(0)
        return ret
    if x == 1:
        ret.append(1)
        return ret

    y = 2

    while ((x / 2) + 1) > y:
        if x % y == 0:
            x /= y
            ret.append(y)
        else:
            y += 1
    ret.append(int(x))
    return ret;

import sys
import time

def usage(exitCode):
    print("python " + sys.argv[0] + " [value] [value]")
    print("\tValues can be in base-ten or base-sixteen (e.g. 0xFF) form")
    print("\tOutput will be in the following form:")
    print("\t\t integer : hex : prime factors : time elapsed in computation")
    sys.exit(exitCode)

if len(sys.argv) != 2 and len(sys.argv) != 3:
    usage(1)

if len(sys.argv) == 2:
    try:
        x = int(sys.argv[1], 0)
    except ValueError:
        print("Cannot get integer values from you input: \"" + sys.argv[1] + "\"")
        usage(-1)
    startTime = time.time()
    sys.stdout.write(str(x) + " : " + hex(x) + " : " + str(primeFactors(x)))
    print(" : " + str(time.time() - startTime))
if len(sys.argv) == 3:
    try:
        x = int(sys.argv[1], 0)
        y = int(sys.argv[2], 0)
    except ValueError:
        print("Cannot get integer values from you input: \"" + sys.argv[1] + "\" \"" + sys.argv[2] + "\"")
        usage(-1)
    if x < y:
        for i in range(x, y):
            startTime = time.time()
            sys.stdout.write(str(i) + " : " + hex(i) + " : " + str(primeFactors(i)))
            print(" : " + str(time.time() - startTime))
    elif x > y:
        for i in range(x, y, -1):
            startTime = time.time()
            sys.stdout.write(str(i) + " : " + hex(i) + " : " + str(primeFactors(i)))
            print(" : " + str(time.time() - startTime))
    else:
        startTime = time.time()
        sys.stdout.write(str(x) + " : " + hex(x) + " : " + str(primeFactors(x)))
        print(" : " + str(time.time() - startTime))
