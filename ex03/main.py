import os
import sys


class NoInputDetected(Exception):
    """no input was detected"""
    pass


class NothingToCompare(Exception):
    """the two string is equal"""
    pass


class NotAStringError(Exception):
    """Not a string in input"""
    pass


def comparaison_mot(mot1, mot2):

    """Compare deux mots et retourne le plus grand
        :param mot1: Permier mot a comparer
        :type mot1: String
        :param mot2: Deuxième mot a comparer
        :type mot2: String
        :return: retourne le mot le plus grand
        :rtype:String
        :raises NotAStringError: Ce qui est rentré n'est pas une string
        :raises NothingToCompare: Les deux mots sont égaux
        :raises NoInputDetected: Un des mots n'a pas été rentré
        :raises TooMuchArgs: Trop d'argument en entrée
        :raises IOError: Le fichier INPUT n'a pas été trouvé
        :raises IndexError: Le fichier INPUT doit être indiqué
    """
    if(mot1 == "" or mot2 == ""):
        raise NoInputDetected
    elif(mot1 == mot2):
        raise NothingToCompare
    elif(isinstance(mot1, str) is False or isinstance(mot2, str) is False):
        raise NotAStringError
    else:
        mot1l = mot1.lower()
        mot2l = mot2.lower()
        i = int(0)
        trouver = False
        lenght1 = len(mot1)
        lenght2 = len(mot2)
        if lenght1 > lenght2:
            max = int(lenght2)
        else:
            max = int(lenght1)
        while trouver == bool(False) and int(i) < int(max):

            if(ord(mot1l[i]) <= ord(mot2l[i])):
                trouver = bool(True)
                resultat = str(mot1)
            elif(ord(mot1l[i]) >= ord(mot2l[i])):
                trouver = bool(True)
                resultat = str(mot2)
            i += 1
        return resultat


def main(line):
    try:
        if len(line.split(";")) > 2:
            raise TooMuchArgs
        else:
            var = line.replace("\n", "")
            var = var.split(";")
            mot1 = str(var[0])
            mot2 = str(var[1])
    except TooMuchArgs:
        print("Bad Input")
    try:
        result = comparaison_mot(mot1, mot2)
        print(result)
    except ValueError:
        print("Bad Input")
    except NotAStringError:
        print("Bad Input")
    except NothingToCompare:
        print("Bad Input")
    except NoInputDetected:
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
