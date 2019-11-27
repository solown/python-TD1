import os
import sys

class InvalidArgsInput(Exception):
    """Raise too much args exception"""

class InvalidSetsType(Exception):
    """Is raise when there is an wrong type in a sets"""

def setsOperation(sets1,sets2): ###Create your custom function here
    setsSub1,setsSub2,setsUnion,setsInter=[],[],[],[]
    setsSums = sets1+sets2
    for item in setsSums:
        if type(item) is not str or len(item)>1:
            raise InvalidSetsType
    if "c" in sets1:
        out1="True"
    else :
        out1="False"
    if "a" in sets2:
        out2="True"
    else :
        out2="False"
    for item in setsSums:
        if item in sets1 and item not in sets2:
            setsSub1.append(item)
        if item in sets2 and item not in sets1:
            setsSub2.append(item)
        if item in sets1 and item in sets2:
            setsUnion.append(item)
        if (item in sets1 and item not in sets2) or (item in sets2 and item not in sets1):
            setsInter.append(item)
    sets1Str = "X : "+formatOutput(sets1)
    sets2Str = "Y : "+formatOutput(sets2)
    out1Str = "c in X : " + str(out1)
    out2Str =  "a in Y : " + str(out2)
    setsSub1Str = "X - Y : " + formatOutput(setsSub1)
    setsSub2Str = "Y - X : " + formatOutput(setsSub2)
    setsUnionStr = "X union Y : " + formatOutput(setsUnion)
    setsInterStr = "X inter Y : " + formatOutput(setsInter)
    return out1Str,out2Str,setsSub1Str,setsSub2Str,setsUnionStr, setsInterStr

def formatOutput(sets):
    setsStr = str(sets).replace("[","{")
    setsStr=setsStr.replace("]","}")
    return setsStr

def main(line):
    try:
        line=line.replace("\n","")
        if line=="NONE":
            setsX = ["a","b","c","d"]
            setsY = ["s","b","d"]
            result=setsOperation(setsX,setsY) ####Change function name and args
            if result == None:
                return
            else:
                for item in result:
                    print(item)
        else:
            raise InvalidArgsInput
    except InvalidArgsInput:
        print("BAD INPUT - Too much args for this programme")
    except InvalidSetsType:
        print("BAD INPUT - Invalid type in sets ")

if __name__=="__main__":
    try:
        inputFile=open(sys.argv[1],"r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND "+sys.argv[1] )
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
