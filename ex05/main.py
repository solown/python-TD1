import os
import sys
class TooMuchArgs(Exception):
    pass

def count():
    for x in range(0,15,3):
        print(x)
    return ""

def main(line):
    try:
        if len(line.split(";"))>0: ###Change number of args need on one line
            raise TooMuchArgs
        else:
            var=line
            result=count() ####Change function name and args
            if result == None:
                return

    except TooMuchArgs:
        print("BAD INPUT - Too much args for this programme")

if __name__=="__main__":
    try:
        inputFile=open(sys.argv[1],"r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND "+sys.argv[1] )
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
