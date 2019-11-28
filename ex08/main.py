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
minute inférieure.
Écrire une procédure tchacatchac qui reçoit la
vitesse du train et qui affiche l’heure du
drame.
Écrire le programme principal qui affiche le tableau
demandé."""


class NegativeInput(Exception):
    """Negative Integer in input is not allowed"""


class InvalidArgsInput(Exception):
    """Too much args in line of input file"""


class WrongTrainSpeed(Exception):
    """Min train speed is above max train speed or conversely"""


def tchacatchac(trainSpeed, dist):
    departureHour = 9
    crashTime = (dist / trainSpeed) * 60
    deathHour = int((crashTime // 60)) + departureHour
    deathMinute = round(crashTime % 60)
    if deathMinute < 10:
        return str(deathHour) + "h0" + str(deathMinute)
    else:
        return str(deathHour) + "h" + str(deathMinute)


def deathHourList(dist, minSpeed, maxSpeed, step):
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
        print("BAD INPUT - Too much args for this programme")
    except ZeroDivisionError:
        print("BAD INPUT - Zero in a division has been found")
    except ValueError:
        print("BAD INPUT - Float or string detected")
    except NegativeInput:
        print("BAD INPUT - Negative input")
    except WrongTrainSpeed:
        print("BAD INPUT - Check max speed and min speed")


if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
