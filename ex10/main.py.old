import os
import sys

class UnvalidListException(Exception):
    """Exception to throw an error when the list contains items out of [0:]"""
class TooMuchArgs(Exception):
    """EXception to throw an error when there is bad args number in input"""
    
def validateList(myList): ###Create your custom function here
    for item in myList:
        if item < 0 or item > 6:
            return False
    return True

def listAdding(myList):
    myList=list(map(int,myList))
    if validateList(myList) == False:
        raise UnvalidListException
    for idx,item in enumerate(myList):
        if item >= 2:
            myList[idx]=item+3
    return myList        
def main(line):
    try:
        if len(line.split(";"))<2: ###Change number of args need on one line
            raise TooMuchArgs
        else:
            var=line.split(";")
            result=listAdding(var) ###Change function name and args
            if result == None:
                return
            else:
                print(result)
    except TooMuchArgs:
        print("BAD INPUT - You didn't respect the needed args for this program")
    except UnvalidListException:
        print("BAD INPUT - Your list doesn't contain only number between 0 and 5")
    except TypeError:
        print("BAD INPUT - Your list may contains str or float instead of integer")
    except ValueError:
        print("BAD INPUT - Your list may contains str or float instead of integer")

if __name__=="__main__":
    try:
        inputFile=open(sys.argv[1],"r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND "+sys.argv[1] )
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
