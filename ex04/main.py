import os
import sys


class NegativePressureInput(Exception):
    """Negative pressure is not allowed"""


class NegativeVolumeInput(Exception):
    """Negative Volume is not allowed"""


class TooMuchArgs(Exception):
    """Too much args in line of input file"""


def pressureChecker(pressure, volume):
    """ Vérifie la pression Sécurisé une enceinte pressurisé
        en fonction des seuils de la pression (pSeuil) et du volume(vSeuil)
        et afficher les consignes/l'état de la machine en fonction des valeurs
        pressure et volume en entrée \n
        :param pressure:la pression présente \n
        :type pressure:float \n
        :param volume:volume que de l'enceinte que nous voulons vérifier \n
        :type volume:float \n
        :return: KO,Augmenter,Diminuer,OK (celon s'il ya  trop de pression) \n
        :rtype: String \n
        :raises NegativeVolumeInput: Le volume entré est négatif \n
        :raises NegativePressureInput: La pression entrée est négative \n

    """

    pSeuil = 2.3
    vSeuil = 7.41
    pressure = float(pressure)
    volume = float(volume)
    if pressure < 0.0:
        raise NegativePressureInput
    if volume < 0.0:
        raise NegativeVolumeInput
    if pressure > pSeuil and volume > vSeuil:
        return "KO"
    elif pressure > pSeuil:
        return "Augmenter"
    elif volume > vSeuil:
        return "Diminuer"
    else:
        return "OK"


def main(line):
    try:
        if len(line.split(";")) > 2:
            raise TooMuchArgs
        else:
            var = line.split(";")
            result = pressureChecker(var[0], var[1])
            if result is None:
                return
            else:
                print(result)
    except TooMuchArgs:
        print("Bad Input")
    except ValueError:
        print("Bad Input")
    except NegativePressureInput:
        print("Bad Input")
    except NegativeVolumeInput:
        print("Bad Input")
    except IndexError:
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
