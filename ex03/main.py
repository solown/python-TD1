import os
import sys


class NoInputDetected(Exception):
    """no input was detected"""
    pass
class NothingToCompare(Exception):
    """the two string is equal"""
    pass
class NotAStringError(Exception):
    pass

def comparaison_mot(mot1,mot2):
    
    if(mot1=="" or mot2=="" ):
        raise NoInputDetected
    elif(  mot1 == mot2):
        raise NothingToCompare
    elif(isinstance(mot1,str)==False or isinstance(mot2,str)==False):
        raise NotAStringError
    else:
        mot1l=mot1.lower()
        mot2l=mot2.lower()
        i=int(0)
        trouver=False
        lenght1=len(mot1)
        lenght2=len(mot2)
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


        return resultat



def main(line):
    try:
        if len(line.split(";"))>2: ###Change number of args need on one line
            raise TooMuchArgs
        else:
            var=line.replace("\n","")
            var=var.split(";")
            mot1=str(var[0])
            mot2=str(var[1])
            try:
                result=comparaison_mot(mot1,mot2) ####Change function name and args
            except ValueError:
                result="BAD INPUT just a value error"
            except NotAStringError:
                result="BAD INPUT It's not a String"
            except NothingToCompare:
                print("It's the same string")
                result="BAD INPUT"
            except NoInputDetected:
                print("Error: NoInputDetected\n *****comparaison_mot***** \n")
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
