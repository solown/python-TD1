import os
import sys
from math import pow,pi


"""
...module::ex06-main
"""

class NegativeOrNullSquareInput(Exception):
    """Negative Volume is not allowed"""


class TooMuchArgs(Exception):
    """Too much args in line of input file"""
# class NullSquareInput(Exception):
    """The square in input is equal to ZERO"""


def cubeCalculator(radius):
    """Fonction qui prend un nombre flottant et calcule sa puissance au cube
        :param radius: un nombre
        :type radius: float
        :return: le cube du nombre
        :rtype: float
        :raises NegativeOrNullSquareInput: Volume négatif
        :raises TooMuchArgs: Trop d'élément en enrtée
        :raises IOError:Erreur fichier INPUT pas trouvé
        :raises IndexError: Erreur fichier INPUT demandé dans l'appel
    """
    radius = float(radius)
    if radius <= 0.0:
        raise NegativeOrNullSquareInput
    cubePow = pow(radius, 3)
    cubePow = round(cubePow,8)
    return cubePow


def volumeSphere(arg1):
    """Utilise la fonction cubeCalculator pour calculer le volume
             d'une sphere. Le rayon est donné en entré. Utilisation du
             module math et de la constante pi
        :param arg1:rayon de la sphère
        :type arg1:float
        :return:retourne le volume
        :rtype:float
    """
    sphereRadius = cubeCalculator(arg1)
    volume = (pi*sphereRadius)/3
    volume = round(volume,8)
    return volume


def main(line):
    try:
        if len(line.split(";")) != 1:
            raise TooMuchArgs
        else:
            var = line
            result = volumeSphere(var)
            if result is None:
                return
            else:
                print(result)
    except TooMuchArgs:
        print("Bad Input")
    except NegativeOrNullSquareInput:
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
