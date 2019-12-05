import os
import sys


"""
...module::ex13-main
"""

def compteMots(chaine):
    """Compte le nombre de mots dans une chaine
        :param chaine: Chaine de caractère choisi
        :type chaine: String
        :return: un dictionnaire avec le compte de chaques mots
        :rtype:dictionnaire
        :raises TooMuchArgs: Trop d'argument en entrée
        :raises IOError:Erreur fichier INPUT pas trouvé
        :raises IndexError: Erreur fichier INPUT demandé dans l'appel
    """
    if (type(chaine) is str):
        dic = {}
        liste = chaine.split()
        for b in liste:
            if (b in dic):
                dic[b] += 1
            else:
                dic[b] = 1
        return dic
    else :
        raise ValueError


def main(line):
    try:
        if len(line.split(";")) != 1:
            raise TooMuchArgs
        else:
            var = line.replace("\n", "")
    except TooMuchArgs:
        print("Bad Input args")
    try:
        int(line)
        print("Bad Input value")
    except ValueError:
        result = compteMots(line)
        if result is not None:
            print(result)
if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
