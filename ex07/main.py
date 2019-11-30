import os
import sys


class TooMuchArgs(Exception):
    pass


class borneError(Exception):
    pass


class FonctionError(Exception):
    """ Fonction name don't right"""
    pass


def maFonction(x):
    if(isinstance(x, int) is not True):
        raise ValueError
    else:
        fonction = 2*x**3+x-5
        int(fonction)
    return fonction


def tabuler(fonction, borneInf, borneSup, nbPas):
    borneInf = int(borneInf)
    borneSup = int(borneSup)
    nbPas = int(nbPas)
    returnList = []
    if (fonction != "maFonction"):
        raise FonctionError
    elif (isinstance(borneInf, int) is not True or
            isinstance(borneSup, int) is not True or
            isinstance(nbPas, int) is not True or
            isinstance(fonction, str) is not True):
        raise ValueError
    elif (borneInf > borneSup):
        raise borneError
    else:
        h = int((borneSup - borneInf)/float(nbPas))
        i = borneInf
        while i <= borneSup:
            y = eval(fonction)(i)
            returnList.append(i)
            returnList.append(y)
            i += h
        return returnList

def main(line):
    try:
        if len(line.split(";")) != 4:
            raise TooMuchArgs
        else:
            var = line.split(";")
            borneInf = (var[0])
            borneSup = (var[1])
            nbPas = (var[2])
            f = var[3].replace("\n","")
    except TooMuchArgs:
        print("Bad Input")
    try:
        result = tabuler(f, borneInf, borneSup, nbPas)
        print(result)
    except FonctionError:
        print("Bad Input")   
    except ValueError:
        print("Bad Input")
    except ZeroDivisionError:
        print("Bad Input")
    except borneError:
        print("Bad Input")
    


if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND "+sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
