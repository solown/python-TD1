import os
import sys
class borneError(Exception):
    pass

def maFonction(x): ###Create your custom function here
    try:

        fonction=2*x**3+x-5
        int(fonction)
    except ValueError:
        fonction="BAD INPUT"
    return fonction

def tabuler(fonction,borneInf,borneSup,nbPas):
    try:
        if (borneInf > borneSup):
            raise borneError
        h= (borneSup - borneInf)/float(nbPas)
        i=borneInf
        while i <= borneSup:
            y=maFonction(i)
            print("x = ",i,"y = ", y)
            i+=h
        resultat=i

    except borneError:
        resultat="Bas INPUT"

def main(line):
    try:
        if len(line.split(";"))>3: ###Change number of args need on one line
            raise TooMuchArgs
        else:
            var=line
            var=var.split(";")
            borneInf=int(var[0])
            borneSup=int(var[1])
            nbPas=float(var[2])
            result=tabuler(maFonction,borneInf,borneSup,nbPas) ####Change function name and args
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
