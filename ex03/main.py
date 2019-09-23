import os
import sys


class NoInputDetected(Exception):
    """no input was detected"""

class NothingToCompare(Exception):
    """the two string is equal"""


def comparaison_mot(mot1,mot2):


    if(mot1=="" or mot2==""):
        raise NoInputDetected
    if(mot1.lower() == mot2.lower()):
        raise NothingToCompare
    mot1l=mot1.lower()
    mot2l=mot2.lower()
    i=int(0)
    trouver=False
    lenght1=len(mot1)
    lenght2=len(mot2)
    try:

        if lenght1>lenght2:
            max=int(lenght2)
        else:
            max=int(lenght1)
        while trouver == bool(False) and int(i)<int(max):

            if(ord(mot1l[i]) <= ord(mot2l[i]) ):
                trouver = bool(True)
                resultat = str(mot1)
            elif(ord(mot1l[i]) >= ord(mot2l[i]) ):
                trouver = bool(True)
                resultat = str(mot2)
            i+=1
    except ValueError:
        resultat="BAD INPUT"
    except NoInputDetected:
        print("Error: NoInputDetected\n *****comparaison_mot***** \n")
        resultat="BAD INPUT"
    except NothingToCompare:
        print("It's the same string")


    return resultat



def main(line):
    try:
        if len(line.split(";"))>2: ###Change number of args need on one line
            raise TooMuchArgs
        else:
            var=line
            var=var.split(";")
            mot1=var[0]
            mot2=var[1]
            result=comparaison_mot(mot1,mot2) ####Change function name and args
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
