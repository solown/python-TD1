import os
import sys
from math import pow,pi


class NegativeOrNullSquareInput(Exception):
    """Negative Volume is not allowed"""


class TooMuchArgs(Exception):
    """Too much args in line of input file"""
# class NullSquareInput(Exception):
    """The square in input is equal to ZERO"""


def cubeCalculator(radius):
    radius = float(radius)
    if radius <= 0.0:
        raise NegativeOrNullSquareInput
    cubePow = pow(radius, 3)
    cubePow = round(cubePow,8)
    return cubePow


def volumeSphere(arg1):
    sphereRadius = cubeCalculator(arg1)
    volume = (pi*sphereRadius)/3
    volume = round(volume,8)
    return volume


def main(line):
    try:
        if len(line.split(";")) != 1:
            raise TooMuchArgs
        else:
            var = line
            result = volumeSphere(var)
            if result is None:
                return
            else:
                print(result)
    except TooMuchArgs:
        print("Bad Input")
    except NegativeOrNullSquareInput:
        print("Bad Input")
    except ValueError:
        print("Bad Input")


if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
