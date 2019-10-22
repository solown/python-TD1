import os
import sys


def compteMots(chaine): ###Create your custom function here

    if (type(chaine) is str):
        dic={}
        liste=chaine.split()
        for b in liste:
            if (b in dic):
                dic[b]+=1
            else:
                dic[b]=1
    else:
        raise ValueError
        dic=null
    return dic

def main(line):
    try:
        if len(line.split(";"))>1: ###Change number of args need on one line
            raise TooMuchArgs
        else:
            var=line.replace("\n","")
            try:
                result=compteMots(line) ####Change function name and args
                for fin in result:
                    print (fin, "....",result[fin])
            except ValueError:
                print("Not a String in input")
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
