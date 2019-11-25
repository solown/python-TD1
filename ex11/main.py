import os
import sys


class NoInputNeeded(Exception):
    """No need input"""
    pass


def liste_comprehension():
    resultat = [i + j for i in "abc" for j in "de"]
    return resultat


def main():
        result = liste_comprehension()
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
