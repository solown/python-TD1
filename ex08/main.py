import os
import sys


"""Je suis ligoté sur les rails en gare d’Arras.
Écrire un programme qui affiche un
tableau me permettant de connaître l’heure à
laquelle je serai déchiqueté par le train parti
de la gare du Nord à 9h (il y a 170 km entre la
gare du Nord et Arras). Le tableau prédira
les différentes heures possibles pour toutes les
vitesses de 100 km/h à 300 km/h, par pas
de 10 km/h, les résultats étant arrondis à la
minute inférieure.\n
Écrire une procédure tchacatchac qui reçoit la
vitesse du train et qui affiche l’heure du
drame.\n
Écrire le programme principal qui affiche le tableau
demandé."""


class NegativeInput(Exception):
    """Negative Integer in input is not allowed"""


class InvalidArgsInput(Exception):
    """Too much args in line of input file"""


class WrongTrainSpeed(Exception):
    """Min train speed is above max train speed or conversely"""


def tchacatchac(trainSpeed, dist):
    """Calcule l'heure à laquelle le M. sera découpé par le train
             en fonction de la vitesse (INT1) et de la distance (INT2)
             à partir de 9h\n
        :param trainSpeed: Vitesse du train\n
        :type trainSpeed: float\n
        :param dist: Distance entre le train et la victime\n
        :type dist: int\n
        :return: donne l'heure quand le train va percuter la victime\n
        :rtype: string\n
        :raises NegativeInput: Entrée négative\n
        :raises InvalidArgsInput: Mauvais argument entré ligne vide.\n
        :raises WrongTrainSpeed:maxSpeed > minSpeed\n
    """
    departureHour = 9
    crashTime = (dist / trainSpeed) * 60
    deathHour = int((crashTime // 60)) + departureHour
    deathMinute = round(crashTime % 60)
    if deathMinute < 10:
        return str(deathHour) + "h0" + str(deathMinute)
    else:
        return str(deathHour) + "h" + str(deathMinute)


def deathHourList(dist, minSpeed, maxSpeed, step):
    """Calcul l'heure du drame\n
            :param dist: Distance entre le train et la victime\n
            :type dist: int\n
            :param minSpeed: vitesse minimum\n
            :type minSpeed: int\n
            :param maxSpeed:Vitesse maximale\n
            :type maxSpeed: int\n
            :param step:fréquence a laquelle on veut avoir l'information\n
            :type step: int\n
            :raises TooMuchArgs: Trop d'argument en entrée\n
            :raises IOError:Erreur fichier INPUT pas trouvé\n
            :raises IndexError: Erreur fichier INPUT demandé dans l'appel\n
    """
    dist, minSpeed = int(dist), int(minSpeed)
    maxSpeed, step = int(maxSpeed), int(step)
    if dist < 0 or minSpeed < 0 or maxSpeed < 0 or step < 0:
        raise NegativeInput
    if maxSpeed < minSpeed:
        raise WrongTrainSpeed
    tabString = "{} km/h -> {} "
    for i in range(minSpeed, maxSpeed, step):
        print(tabString.format(i, tchacatchac(i, dist)))


def main(line):
    try:
        line = line.replace("\n", "")
        if line == "NONE":
            result = deathHourList(170, 100, 300, 10)
            if result is None:
                return
            else:
                print(result)
        else:
            raise InvalidArgsInput
    except InvalidArgsInput:
        print("Bad Input")
    except ZeroDivisionError:
        print("Bad Input")
    except ValueError:
        print("Bad Input")
    except NegativeInput:
        print("Bad Input")
    except WrongTrainSpeed:
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
