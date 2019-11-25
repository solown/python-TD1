import os
import sys


class TooMuchArgs(Exception):
    """Raise too much args exception"""


class InvalidSetsType(Exception):
    """Is raise when there is an wrong type in a sets"""


def setsOperation(sets1, sets2):
    setsSub1, setsSub2, setsUnion, setsInter = [], [], [], []
    setsSums = sets1 + sets2
    for item in setsSums:
        if type(item) is not str or len(item) > 1:
            raise InvalidSetsType
    print(sets1, sets2)
    if "c" in sets1:
        out1 = "True"
    else:
        out1 = "False"
    if "a" in sets2:
        out2 = "True"
    else:
        out2 = "False"
    for item in setsSums:
        if item in sets1 and item not in sets2:
            setsSub1.append(item)
        if item in sets2 and item not in sets1:
            setsSub2.append(item)
        if item in sets1 and item in sets2:
            setsUnion.append(item)
        if (item in sets1 and item not in sets2) or
        (item in sets2 and item not in sets1):
            setsInter.append(item)
    return out1, out2, setsSub1, setsSub2, setsUnion, setsInter


def main(line):
    try:
        var = line.split(";")
        if len(var) > 2:
            raise TooMuchArgs
        else:
            var[1] = var[1].replace("\n", "")
            setsX, setsY = var[0].split(","), var[1].split(",")
            result = setsOperation(setsX, setsY)
            print(result)
    except TooMuchArgs:
        print("BAD INPUT - Too much args for this programme")
    except InvalidSetsType:
        print("BAD INPUT - Invalid type in sets ")

if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
