import os
import sys

"""
...module::ex01-main
"""


class NegativeInput(Exception):
    pass


def calcul_vitesse(temps, distance):

    """Calcul la vitesse
        :param temps: temps mis pour parcourir la distance
        :type temps:float
        :param distance: distance parcourue
        :type distance: float
        :return: retourne la vitesse
        :rtype: float
        :raises NegativeInput: on entre un nombre négatif
        :raises TooMuchArgs: Trop d'argument en entrée
        :raises ZeroDivisionError: La distance est négative
        :raises ValueError: Mauvais type
        :raises IOError: Le fichier INPUT n'a pas été trouvé
        :raises IndexError: Fichier INPUT pas spécifié
    """
    if (float(temps) == 0):
        raise ZeroDivisionError
    elif (isinstance(float(temps), float) is False or
          isinstance(float(distance), float) is False):
        raise ValueError
    elif((float(temps) < 0) or (float(distance) < 0)):
        raise NegativeInput
    else:
        temps = float(temps)
        distance = float(distance)
        vitesse = round(distance / temps, 1)

    return vitesse


def main(line):
    try:
        if len(line.split(";")) != 2:
            raise TooMuchArgs
        else:
            var = line
            var = var.split(";")
            temps = var[0]
            distance = var[1]
    except TooMuchArgs:
        print("Bad Input")
    try:
        result = calcul_vitesse(temps, distance)
        print(result)
    except ZeroDivisionError:
        print("Bad Input")
    except NegativeInput:
        print("Bad Input")
    except ValueError:
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
