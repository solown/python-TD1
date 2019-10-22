import os
import sys
class TooMuchArgs(Exception):
    pass
class borneError(Exception):
    pass
class FonctionError(Exception):
    """ Fonction name don't right"""
    pass
def maFonction(x): ###Create your custom function here

    if(isinstance(x,int)!=True):
        raise ValueError
    else:
        fonction=2*x**3+x-5
        int(fonction)

    return fonction

def tabuler(fonction,borneInf,borneSup,nbPas):
    borneInf=int(borneInf)
    borneSup=int(borneSup)
    nbPas=int(nbPas)
    if (fonction != "Mafonction"):
        raise FonctionError
    elif (isinstance(borneInf,int)!=True or isinstance(borneSup,int)!=True or isinstance(nbPas,int)!=True or isinstance(fonction,str)!=True):
        raise ValueError
    elif (borneInf > borneSup):
        raise borneError
    else:
        h=int((borneSup - borneInf)/float(nbPas))
        i=borneInf
        while i <= borneSup:
            y=eval(fonction)(i)
            print("x = ",i,"y = ", y)
            i+=h
        resultat=i
        return resultat


def main(line):
    try:
        if len(line.split(";"))>4: ###Change number of args need on one line
            raise TooMuchArgs
        else:

            var=line.split(";")
            borneInf=(var[0])
            borneSup=(var[1])
            nbPas=(var[2])
            f=var[3]
            try:
                result=tabuler(f,borneInf,borneSup,nbPas) ####Change function name and args
            except FonctionError:
                print("Not the good fonction name her: maFonction and not ",f)
                result="BAD INPUT"
            except ValueError:
                print("Just a Value error \n")
                result="BAD INPUT"
            except ZeroDivisionError:
                print("You can't / by 0")
                result="BAD INPUT"
            except borneError:
                print("The borneInf can't be taller than borneSup")
                result="BAD INPUT"


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
