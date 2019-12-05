import os
import sys


"""
...module::ex01-main
"""

class InvalidArgsInput(Exception):
    """Raise too much args exception"""


class InvalidSetsType(Exception):
    """Is raise when there is an wrong type in a sets"""


def setsOperation(sets1, sets2):
    """Exécute les opérations demandées.
        :param sets1: première liste x
        :type sets1: liste
        :param sets2:deuxième liste y
        :type sets2:liste
        :return: Les string de chaque opérations
        :rtype: str
        :raises TooMuchArgs: Trop d'argument en entrée
        :raises IOError:Erreur fichier INPUT pas trouvé
        :raises IndexError: Erreur fichier INPUT demandé dans l'appel
        :raises invalidArgsInput:Trop d'argument en entré
        :raises InvalidSetsType:mauvais type des sets

    """
    setsSub1, setsSub2, setsUnion, setsInter = [], [], [], []
    setsSums = sets1 + sets2
    for item in setsSums:
        if type(item) is not str or len(item) > 1:
            raise InvalidSetsType
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
        if ((item in sets1 and item not in sets2) or
                (item in sets2 and item not in sets1)):
            setsInter.append(item)
    sets1Str = "X : "+formatOutput(sets1)
    sets2Str = "Y : "+formatOutput(sets2)
    out1Str = "c in X : " + str(out1)
    out2Str = "a in Y : " + str(out2)
    setsSub1Str = "X - Y : " + formatOutput(setsSub1)
    setsSub2Str = "Y - X : " + formatOutput(setsSub2)
    setsUnionStr = "X union Y : " + formatOutput(setsUnion)
    setsInterStr = "X inter Y : " + formatOutput(setsInter)
    return (out1Str, out2Str, setsSub1Str, setsSub2Str,
            setsUnionStr, setsInterStr)


def formatOutput(sets):
    """Met en forme les listes.
        :param sets:la chaine de caractère
        :type sets:liste
        :return:chaine de caractère ayant plus les []
        :rtype:string
    """
    setsStr = str(sets).replace("[", "{")
    setsStr = setsStr.replace("]", "}")
    return setsStr


def main(line):
    try:
        line = line.replace("\n", "")
        if line == "NONE":
            setsX = ["a", "b", "c", "d"]
            setsY = ["s", "b", "d"]
            result = setsOperation(setsX, setsY)
            if result is None:
                return
            else:
                for item in result:
                    print(item)
        else:
            raise InvalidArgsInput
    except InvalidArgsInput:
        print("Bad Input")
    except InvalidSetsType:
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
