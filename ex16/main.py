import os
import sys


class InvalidInputType(Exception):
    """Raise exception when receving a string in input"""


class InvalidArgsInput(Exception):
    """Raise an exception the number of args in input is incorrect"""


class NegativeInput(Exception):
    """Raise an exception when there is a negative int in input"""


class Vecteur2D:
    """class Vecteur2D\n
        :raises TooMuchArgs: Trop d'argument en entrée\n
        :raises IOError:Erreur fichier INPUT pas trouvé\n
        :raises IndexError: Erreur fichier INPUT demandé dans l'appel\n
    """
    def __init__(self, x, y):
        """constructer de la class Vecteur2D\n
            :param x:Coordonnée x d'un vecteur\n
            :param y:coordonnée y d'un vecteur\n
            :type x:int\n
            :type y:int\n
            :raises NegativeInput: vous avez entré une vlaeu négative\n
            :raises InvalidInputType: ce que vous avez entré n'est pas un int\n

        """
        if (str(x).isdigit() and str(y).isdigit()):
            if(int(x) >= 0 and int(y) >= 0):
                self.x = int(x)
                self.y = int(y)
            else:
                raise NegativeInput
        else:
            raise InvalidInputType

    def vectorSum(self, vect2):
        """Faire la somme de deux vecteurs\n
            :param vect2 objet Vecteur2D\n
            :type vect2: class:'Vecteur2D'\n
            :rtype: class:'Vecteur2D'\n
            :return:la somme de deux vecteur\n
        """
        xSum = self.x + vect2.x
        ySum = self.y + vect2.y
        return Vecteur2D(xSum, ySum)

    def getX(self):
        """Obtenir la valeur de x d'un objet vecteur 2D\n
            :rtype:int\n
            :return: la valeur d'un x d'un Vecteur\n
        """
        return self.x

    def getY(self):
        """Obtenir la valeur de y d'un objet vecteur 2D\n
            :return: la valeur d'un y d'un vecteur\n
            :rtype:int\n

        """
        return self.y

    def getVector(self):
        """Obtenir la valeur d'un objet Vecteur2D\n
            :return: coordonnées d'un vecteur\n
            :rtype:int,int\n
        """
        return self.getX(), self.getY()


def main(line):
    try:
        if len(line.split(",")) != 2:
            raise InvalidArgsInput
        else:
            line = line.split(",")
            line[-1] = line[-1].replace("\n", "")
            var1, var2 = line[0].split(";")
            var3, var4 = line[1].split(";")
    except InvalidArgsInput:
        print("Bad Input")
        return
    except IndexError:
        print("Bad Input")
        return
    try:
        a = Vecteur2D(var1, var2)
        b = Vecteur2D(var3, var4)
        c = a.vectorSum(b)
        print("v1 : " + str(a.getVector()))
        print("v2 : " + str(b.getVector()))
        print("somme : " + str(c.getVector()))
    except InvalidInputType:
        print ("Bad Input")
    except NegativeInput:
        print("Bad Input")
    except ValueError:
        print("Bad Innput")


if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
        print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
        print("BAD USAGE --> USAGE : python3 main.py inputfile")
