import os
import sys


"""
...module::ex11-main
"""

class InvalidArgsInput(Exception):
    """No need input"""
    pass


def liste_comprehension():
    """affiche  toutes les possibilités
             de combinaison entre les
             caractère de la chaine 'abc' et
             'de'
        :return: La lsite de toutes les possibilités
        :rtype: liste
        :raises TooMuchArgs: Trop d'argument en entrée
        :raises IOError:Erreur fichier INPUT pas trouvé
        :raises IndexError: Erreur fichier INPUT demandé dans l'appel
    """
    resultat = [i + j for i in "abc" for j in "de"]
    return resultat


def main(line):
    try:
        line = line.replace("\n", "")
        if line == "NONE":
            result = liste_comprehension()
            print(result)
        else:
            raise InvalidArgsInput
    except InvalidArgsInput:
        print("Bad Input")
    except TypeError:
        print("Bad Input")
    except ValueError:
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
