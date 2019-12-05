import os
import sys


"""
...module::ex15-main
"""

class TooMuchArgs(Exception):
    """ Trop d'argument en entrée"""
    pass


class NotANumberError(Exception):
    """not a number in input"""
    pass


class Vecteur2D:
    """class Vecteur2D
    """
    def __init__(self, x=0, y=0):
        """Cosntructeur de la classe
            :param x: coordonée x du vecteur par defaut à 0
            :type x: int
            :param y:cooronnée y du vecteur par defaut à 0
            :type y:int
            :raises NotANumberError:Ce n'est pas un int en entrée
            :raises TooMuchArgs: Trop d'argument en entrée
            :raises IOError:Erreur fichier INPUT pas trouvé
            :raises IndexError: Erreur fichier INPUT demandé dans l'appel
        """
        if (x != 0 and y != 0):
            if (x.isdigit() and y.isdigit()):
                self.x = x
                self.y = y
            else:
                raise NotANumberError
        else:
            self.x = x
            self.y = y


def main(line):
    try:
        if len(line.split(";")) != 2:
            raise TooMuchArgs
        else:
            line = line.replace("\n","")
            line = line.split(";")
            var1 = line[0]
            var2 = line[1]
    except TooMuchArgs:
        print("Bad Input")
        return
    try :
        a = Vecteur2D()
        coordA = (a.x,a.y)
        print("par défaut : "+ str(coordA))
        b = Vecteur2D(var1, var2)
        coordB = (b.x,b.y)
        print("instance : " + str(coordB))
    except NotANumberError:
        print ("Bad Input")


if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
