import os
import sys


def liste_comprehension(): ###Create your custom function here
    resultat= [ i+j for i in "abc" for j in "de"]
    return resultat

def main():
    result=liste_comprehension() ####Change function name and args
    print(result)

if __name__=="__main__":
    main()
