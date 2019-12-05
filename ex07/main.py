import os
import sys


class TooMuchArgs(Exception):
    """ You put too much input """
    pass


class BorneError(Exception):
    """Biger born lower than the lower one"""
    pass


class FonctionError(Exception):
    """ Fonction name don't right"""
    pass


def maFonction(x):
    """Calcul le resultat de la fonction y = 2x ^ 3 + x - 5
        :param x:valeur de x
        :type x:float
        :return: retourne f(x)
        :rtype: float

    """
    if(isinstance(x, int) is not True):
        raise ValueError
    else:
        fonction = 2 * x ** 3 + x - 5
        int(fonction)
    return fonction


def tabuler(fonction, borneInf, borneSup, nbPas):
    """Calcul les valeurs on se rapproche d'une valeur avc un certain pas
        :param fonction: nom de la fonction que l'on veut utiliser
        :type fonction: string
        :param borneInf: borne inferieur des recherches
        :type borneInf: int
        :param borneSup: borne supérieur des recherches
        :type borneSup:int
        :param nbPas:fréquence a laquelle on veut se rapprocher
        :type nbPas: int
        :return: Liste des valeurs
        :rtype:liste
        :raises ValueError: x n'est pas un int
        :raises FonctionError: la focntion n'est pas trouvée
        :raises BorneError: borneInf > borneSup
        :raises TooMuchArgs: Trop d'argument en entrée
        :raises IOError:Erreur fichier INPUT pas trouvé
        :raises IndexError: Erreur fichier INPUT demandé dans l'appel
    """

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
        raise BorneError
    else:
        h = int((borneSup - borneInf) / float(nbPas))
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
            f = var[3].replace("\n", "")
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
    except BorneError:
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
