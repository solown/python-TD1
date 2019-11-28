import os
import sys


class UnvalidListException(Exception):
    """Exception to throw an error when the list contains items out of [0:]"""


class InvalidArgsInput(Exception):
    """EXception to throw an error when there is bad args number in input"""


def validateList(myList):
    for item in myList:
        if item < 0 or item > 6:
            return False
    return True


def listAdding(myList):
    myList = list(map(int, myList))
    if validateList(myList) is False:
        raise UnvalidListException
    for idx, item in enumerate(myList):
        if item >= 2:
            myList[idx] = item + 3
    return myList


def main(line):
    try:
        line = line.replace("\n", "")
        if line == "NONE":
            myList = [0, 4, 3, 1, 2, 4, 3, 1]
            result = listAdding(myList)
            if result is None:
                return
            else:
                print(result)
        else:
            raise InvalidArgsInput
    except InvalidArgsInput:
        print("BAD INPUT \
                You didn't respect the needed args for this program")
    except UnvalidListException:
        print("BAD INPUT")
        print("- Your list doesn't contain only number between 0 and 5")
    except TypeError:
        print("BAD INPUT")
        print("- Your list may contains str or float instead of integer")
    except ValueError:
        print("BAD INPUT")
        print("- Your list may contains str or float instead of integer")


if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
