import os
import sys


"""
...module::ex14-main
"""

class UndefinedAttributes(Exception):
    """Raise an exception if an attribute in undefined"""


class InvalidArgsInput(Exception):
    """Raise an exception the number of args in input is incorrect"""


class maClasse():
    """Class maClasse qui affiche le resultat d'une somme
        :raises UndefinedAttributes: Attribut pas définis
        :raises InvalidArgsInput: Argument en entré ne sont aps valide.
        :raises TooMuchArgs: Trop d'argument en entrée
        :raises IOError:Erreur fichier INPUT pas trouvé
        :raises IndexError: Erreur fichier INPUT demandé dans l'appel
    """
    x = 23
    y = x + 5

    def __init__(self):
        """Constructeur """
        self.z = 42

    def affiche(self):
        """Affiche le resultat de la somme
            :return:Retourne la somme
            :rtype:(int,int)
        """
        return(self.y, self.z)


def main(line):
    try:
        line = line.replace("\n", "")
        if line == "NONE":
            myObj = maClasse()
            result = myObj.affiche()
            if result is not None:
                print(result)
        else:
            raise InvalidArgsInput
    except InvalidArgsInput:
        print("Bad Input")
    except (ValueError, TypeError) as e:
        print("Bad Input")


if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
