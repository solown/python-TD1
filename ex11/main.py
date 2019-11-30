import os
import sys


class InvalidArgsInput(Exception):
    """No need input"""
    pass


def liste_comprehension():
    resultat = [i + j for i in "abc" for j in "de"]
    return resultat


def main(line):
    try:
        line = line.replace("\n", "")
        if line == "NONE":
            result = liste_comprehension()
            print(result)
        else:
            raise InvalidArgsInput
    except InvalidArgsInput:
        print("Bad Input")
    except TypeError:
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
        
