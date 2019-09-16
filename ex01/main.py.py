

def calcul_vitesse():


    """
    Fonction qui calcul la vitesse.
        Demande à l'utilisateur de rentrer:
        1 float temps
        1 float distance
        Puis elle calcul la vitesse
    Elle affiche la vitesse en float.

    Eception renvoyé:
        Si division par 0: BAD INPUT
        Si entrée autre que float: BAD INPUT
    """
    try:
        temps=(float(input("Entrer le temps en heure ")))
        distance=(float(input("Entrer une distance en kilomètre ")))
        vitesse=round(distance/temps,1)

    except ZeroDivisionError:
        print("Can't divide by 0:\n ex01.py \n ")
        vitesse = "BAD INPUT"
    except ValueError:

        print("Somthing wrong with what you put in... \n ex01.py \n")
        vitesse="BAD INPUT"

    return vitesse
res=calcul_vitesse()
print(res "km/h")
