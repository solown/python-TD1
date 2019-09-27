import os
import sys
import math as m

class NegativeOrNullSquareInput(Exception):
    """Negative Volume is not allowed"""
class TooMuchArgs(Exception):
    """Too much args in line of input file"""
class NullSquareInput(Exception):
    """The square in input is equal to ZERO"""

def cubeCalculator(radius): ###Create your custom function here
    radius=float(radius)
    if radius<=0.0:
        raise NegativeOrNullSquareInput
    return m.pow(radius,3)

def volumeSphere(arg1):
    sphereRadius = cubeCalculator(arg1)
    volume = (m.pi*sphereRadius)/3
    return volume

def main(line):
    try:
        if len(line.split(";"))>1: ###Change number of args need on one line
            raise TooMuchArgs
        else:
            var=line
            result=volumeSphere(var) ####Change function name and args
            if result == None:
                return
            else:
                print(result)
    except TooMuchArgs:
        print("BAD INPUT - Too much args for this programme")
    except NegativeSquareOrNullInput:
        print("BAD INPUT - Negative square in input")
    except ValueError:
        print("BAD INPUT - String has been found")

if __name__=="__main__":
    try:
        inputFile=open(sys.argv[1],"r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND "+sys.argv[1] )
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")

