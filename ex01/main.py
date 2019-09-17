import os
import sys




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
    try:
        temps=float(temps)
        distance=float(distance)
        vitesse=round(distance/temps,1)

    except ZeroDivisionError:
        print("Can't divide by 0:\n ex01.py \n ")
        vitesse = "BAD INPUT"
    except ValueError:

        print("Somthing wrong with what you put in... \n ex01.py \n")
        vitesse="BAD INPUT"

    return vitesse


def main(line):
    try:

        if len(line.split(";"))>2: ###Change number of args need on one line
            raise TooMuchArgs
        else:
            var=line
            var=var.split(";")
            temps=var[0]
            distance=var[1]

            result=calcul_vitesse(temps,distance) ####Change function name and args
            if result == None:
                return
            else:
                print(result )
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
