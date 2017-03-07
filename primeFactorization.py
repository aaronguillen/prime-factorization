#Aaron Guillen
#October 2016

#This is going to be a simple (and, hopefully, clever) program to find prime factors

def primeFactors(x):
    "This function returns a list of the prime factors of our parameter"
    #We begin with an empty list
    ret = []

    #Check for strange inputs, viz. x <= 1
    if x < 0: #Add -1 to our list of factors, negate x and work with it anyhow
        ret.append(-1)
        x *= -1
    elif x == 0: #I mean, I guess zero is the only factor or zero
        ret.append(0)
        return ret
    #if, not elif, because we want our factors for x = -1 to be 1 and -1
    if x == 1: #One is unique, ya know. It's factors are itself
        ret.append(1)
        return ret

    #Alright, so we begin with 2 because it's the first prime number
    y = 2

    #We only need to check up to half of x. After that, y won't ever divide x
    while ((x / 2) + 1) > y: #Or, I suppose not (y > x / 2)
        #So if our current y divides x, update x by doing said division
        if x % y == 0:
            x /= y
            #Then add y to our list of factors
            ret.append(y)
        else:
            #Otherwise, check the next number up
            y += 1
        #We'll always skip non primes because their requisite primes will
        #already have been checked and divided out
        #(e.g., a number divisible by 4 will not have 4 added to its list
        #of factors because 2 will have added twice and it will have been
        #divided by 2 twice by the time we check 4)
    #Whatever's left still needs to be appended
    ret.append(int(x))
    return ret;

import sys
import time

#You know I like my usage ..
def usage(exitCode):
    print("python " + sys.argv[0] + " [value] [value]")
    print("\tValues can be in base-ten or base-sixteen (e.g. 0xFF) form")
    print("\tOutput will be in the following form:")
    print("\t\t integer : hex : prime factors : time elapsed in computation")
    sys.exit(exitCode)

def organizePrint(x):
    startTime = time.time()
    sys.stdout.write(str(x) + " : " + hex(x) + " : " + str(primeFactors(x)))
    print(" : " + str(time.time() - startTime))

if len(sys.argv) != 2 and len(sys.argv) != 3:
    usage(1)

try:
    x = int(sys.argv[1], 0) #int(stringValue, 0) adding this second parameter, this zero, tells Python to guess the base, allowing hex input such as 0xFF
except ValueError: #They give us input that cannot be parsed to an integer
    print("Cannot get integer values from you input: \"" + sys.argv[1] + "\"")
    usage(-1)

#Allow command line input
if len(sys.argv) == 2: #If we have one input from the command line
    organizePrint(x)
else: #If we have two inputs from the command line.
    try:
        y = int(sys.argv[2], 0)
    except ValueError:
        print("Cannot get integer values from you input: \"" + sys.argv[2] + "\"")
        usage(-1)
    if x < y: #We're going to allow input from low to high or high to low
        for i in range(x, y):
            organizePrint(i)
    elif x > y:
        for i in range(x, y, -1): #Step down if input is high to low
            organizePrint(i)
    else: #The numbers they provided are the same
        organizePrint(x)

#If we want to simply remove any non digit-values from our command line input (or any string)
#I don't actually use this, but it's here if you don't want to deal with
#exception handling
#just add something like x = int(removeAlpha(sys.argv[1]))
def removeAlpha(inStr):
    for i in inStr:
        if not str(i).isdigit():
            inStr = inStr.replace(i, "")
    return inStr

#for i in range (0xFFFFFFF0, 0xFFFFFFFF):
#    startTime = time.time()
#    sys.stdout.write(str(i) + " : " + hex(i) + " : " + str(primeFactors(i)))
#    print(" : " + str(time.time() - startTime))
