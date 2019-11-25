import os
import sys


class NoInputNeeded(Exception):
    """No need input"""
    pass


def fonction_liste():
    liste = [17, 38, 10, 25, 72]
    liste.sort()
    print("Liste triée:\n")
    print(liste, "\n")
    liste.append(12)
    print("Liste avec un ajout de 12:\n")
    print(liste, "\n")
    liste.reverse()
    print("Liste renversée:\n")
    print(liste, "\n")
    print("index du nombre 17 de la liste:\n")
    print(liste.index(17), "\n")
    liste.remove(38)
    print("Liste sans 38:\n")
    print(liste, "\n")
    print("nombre du deuxième au 3ème élément:\n")
    print(liste[2:3], "\n")
    print("affichez la sous-liste du début au 2e élément:\n")
    print(liste[:2], "\n")
    print("affichez la sous-liste du 3e élément à la fin de la liste:\n")
    print(liste[3:], "\n")
    print("affichez la sous-liste complète de la liste:\n")
    print(liste[:], "\n")
    print("affichez le dernier élément en utilisant un indexage négatif.\n")
    print(liste[-1], "\n")
    return liste


def main():

    result = fonction_liste()
    if result is None:
        return
    else:
        print(result)

if __name__ == "__main__":
    try:
        if (sys.argv[1] != ""):
            raise NoInputNeeded
    except NoInputNeeded:
        print("you don't have to say anything")
        result = "BAD INPUT"
    except IndexError:
        main()
