import os
import sys


class NegativeInput(Exception):
    pass


def calcul_vitesse(temps, distance):

    """Calcul la vitesse \n
        :param temps: temps mis pour parcourir la distance \n
        :type temps:float \n 
        :param distance: distance parcourue \n
        :type distance: float \n
        :return: retourne la vitesse \n
        :rtype: float \n
        :raises NegativeInput: on entre un nombre négatif \n
        :raises ZeroDivisionError: La distance est négative \n
        :raises ValueError: Mauvais type \n
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
