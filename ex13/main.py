import os
import sys


def compteMots(chaine):
    if (type(chaine) is str):
        dic = {}
        liste = chaine.split()
        for b in liste:
            if (b in dic):
                dic[b] += 1
            else:
                dic[b] = 1
        return dic
    else :
        raise ValueError


def main(line):
    try:
        if len(line.split(";")) != 1:
            raise TooMuchArgs
        else:
            var = line.replace("\n", "")
    except TooMuchArgs:
        print("Bad Input args")
    try:
        result = compteMots(line)
        if result is not None:
            print(result)
    except ValueError:
        print("Bad Input value")

if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
