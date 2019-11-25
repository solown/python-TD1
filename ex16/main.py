import os
import sys


def fcnt1(arg1,arg2,...):


def main(line):
    try:
        if len(line.split(";")) > 1:
            raise TooMuchArgs
        else:
            var = line
            result=yourbeautifulFctn(var)
            if result is None:
                return
            else:
                print(result)
    except TooMuchArgs:
        print("BAD INPUT - Too much args for this programme")

if __name__=="__main__":
    try:
        inputFile=open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
