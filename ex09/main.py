import os
import sys


class NoInputNeeded(Exception):
    """No need input"""
    pass


def fonction_liste():
    """FAit des manipulation sur une liste\n
        :return: retourne une liste contenant ces manipulations\n
        :rtype: liste\n
        :raises NoInputNeeded: Erreur car il y a pas besoin d'entré\n
        :raises TooMuchArgs: Trop d'argument en entrée\n
        :raises IOError:Erreur fichier INPUT pas trouvé\n
        :raises IndexError: Erreur fichier INPUT demandé dans l'appel\n
    """
    liste = [17, 38, 10, 25, 72]
    returnList=[]
    liste.sort()
    sortedList = liste[:]
    returnList.append(sortedList)
    sortedList.append(12)
    returnList.append(sortedList)
    reversedList = sortedList[:]
    reversedList.reverse()
    returnList.append(reversedList)
    returnList.append(reversedList.index(17))
    reducedList = reversedList[:]
    reducedList.remove(38)
    returnList.append(reducedList)
    returnList.append(reducedList[2:3])
    returnList.append(reducedList[:2])
    returnList.append(reducedList[3:])
    returnList.append(reducedList[:])
    returnList.append(reducedList[-1])
    return returnList


def main(line):
    try:
        line = line.replace("\n", "")
        if line == "NONE":
            result = fonction_liste()
            for item in result:
                print(item)
    except IndexError:
        print("Bad Input")

if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in  inputFile:
            main(line)
    except NoInputNeeded:
        print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
        print("BAD USAGE --> USAGE : python3 main.py inputfile")
