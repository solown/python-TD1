import os
import sys


def pressureChecker(pressure,volume):
    pSeuil = 2.3
    vSeuil = 7.41
    try:
        pressure=float(pressure)
        volume=float(volume)
        assert pressure<0.0
        assert volume<0.0
        if pressure > pSeuil && volume > vSeuil:
            return "Arrêt immédiat"
        elif pressure > pSeuil:
            return "Diminuer le seuil"
        elif volume > vSeuil:
            return "Diminuer le volume"
    except ValueError:
        print("BAD INPUT")
    except AssertionError:
        print("BAD INPUT -> Seuil négatif")

def main(line):
    try:
        if len(line.split(";"))>2: ###Change number of args need on one line
            raise TooMuchArgs
        else:
            var=line.split(";")
            result=pressureChecker(var[0],var[1]) ####Change function name and args
            if result == None:
                return
            else:
                print(result)
    except TooMuchArgs:
        print("BAD INPUT - Too much args for this programme")

if __name__=="__main__":
    try:
        inputFile=open(sys.argv[1],"r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND "+sys.argv[1] )
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")

