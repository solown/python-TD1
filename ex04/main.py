import os
import sys


class NegativePressureInput(Exception):
    """Negative pressure is not allowed"""


class NegativeVolumeInput(Exception):
    """Negative Volume is not allowed"""


class TooMuchArgs(Exception):
    """Too much args in line of input file"""


def pressureChecker(pressure, volume):
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
