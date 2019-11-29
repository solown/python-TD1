import os
import sys


class NegativeInput(Exception):
    pass


def calcul_vitesse(temps, distance):

    """
    Fonction qui calcul la vitesse.
        Demande à l'utilisateur de rentrer:
        1 float temps
        1 float distance
        Puis elle calcul la vitesse
    Elle affiche la vitesse en float.

    Eception renvoyé:
        Si division par 0: BAD INPUT
        Si entrée autre que float: BAD INPUT
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
