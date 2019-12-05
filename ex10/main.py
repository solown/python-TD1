import os
import sys


class UnvalidListException(Exception):
    """Exception to throw an error when the list contains items out of [0:]"""


class InvalidArgsInput(Exception):
    """EXception to throw an error when there is bad args number in input"""


def validateList(myList):
    """Valide la liste celon l'énnoncé
        :param myList: Liste entrée
        :type myList: Liste
        :raises TooMuchArgs: Trop d'argument en entrée
        :raises IOError:Erreur fichier INPUT pas trouvé
        :raises IndexError: Erreur fichier INPUT demandé dans l'appel
        :return: Soit un true soit un False
        :rtype: bool
    """
    for item in myList:
        if item < 0 or item > 6:
            return False
    return True


def listAdding(myList):
    """Permet d'ajouter ou des éléments dans une liste
        :param myList: Liste entré
        :type myList:Liste
        :return: Retourne la liste après traitement
        :rtype: Liste
        :raises UnvalidListException: La liste n'est pas valide
    """
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
        print("Bad Input")
    except UnvalidListException:
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
