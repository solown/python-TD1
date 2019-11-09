import os
import sys


def validateList(myList): ###Create your custom function here
        
def listAdding(myList):
    if validateList == False:
        raise UnvalidListException
    for idx,item in enumerate(myList):
        if item >= 2:
            myList[idx]=item+3
            
def main(line):
    try:
        if len(line.split(";"))<2: ###Change number of args need on one line
            raise TooMuchArgs
        else:
            var=line
            result=yourbeautifulFctn(var) ####Change function name and args
            if result == None:
                return
            else:
                print(result)
    except TooMuchArgs:
        print("BAD INPUT - You didn't respect the needed args for this program")
    except UnvalidListException:
        print("BAD INPUT - Your list doesn't contain only number between 0 and 5")


if __name__=="__main__":
    try:
        inputFile=open(sys.argv[1],"r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND "+sys.argv[1] )
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
