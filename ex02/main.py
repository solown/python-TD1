import os
import sys
import math as m


class NegativeFloatExcept(Exception):
    """Exception for negative float in input"""


class TooMuchArgs(Exception):
    """Exception for too much args"""


class BadTypeinFile(Exception):
    """Exception for string in INPUT.TXT"""


def squareCalculator(floatNum):
    if floatNum.isdigit():
        #raise BadTypeinFile
        return
    else:
        floatNum = float(floatNum)
        if floatNum < 0.0:
                raise NegativeFloatExcept
        else:
            squareFloatNum = m.sqrt(floatNum)
            return squareFloatNum


def main(line):
    try:
        if len(line.split(";")) > 1:
            raise TooMuchArgs
        else:
            floatNum = line
            result = squareCalculator(floatNum)
            if result is None:
                return
            else:
                print(result)
    except TooMuchArgs:
        print("BAD INPUT - Too much args for this programme")
    except ValueError:
        print("BAD INPUT for " + str(floatNum))
    except NegativeFloatExcept:
        print("BAD INPUT for " + str(floatNum))
    except ValueError:
        print("BAD INPUT")
    """ except BadTypeinFile:
        print("BAD INPUT")"""


if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
