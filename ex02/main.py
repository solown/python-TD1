import os
import sys
import math as m

class NegativeFloatExcept(Exception):
    """Exception for negative float in input"""

def squareCalculator(floatNum):
    try:
        floatNum=float(floatNum)
        if floatNum < 0.0:
            raise NegativeFloatExcept
        squareFloatNum=m.sqrt(floatNum)
    except ValueError:
        print("BAD INPUT for " + str(floatNum))
    except NegativeFloatExcept:
        print("BAD INPUT for " +str(floatNum))

def main(line):
    floatList = line.split(";")
    for floatNum in floatList:
        squareCalculator(floatNum)

if __name__=="__main__":
    try:
        inputFile=open(sys.argv[1],"r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND "+sys.arv[1] )
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
