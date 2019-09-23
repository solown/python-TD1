class NoInputDetected(Exception):
    pass
class NothingToCompare(Exception):
    pass


def comparaison_mot():

    mot1=(str(input("Entrer un mot: ")))
    mot2=(str(input("Entrer un mot: ")))
    if(mot1=="" or mot2==""):
        raise NoInputDetected
    if(mot1.lower() == mot2.lower()):
        raise NothingToCompare
    mot1l=mot1.lower()
    mot2l=mot2.lower()
    i=int(0)
    trouver=False
    lenght1=len(mot1)
    lenght2=len(mot2)
    try:

        if lenght1>lenght2:
            max=int(lenght2)
        else:
            max=int(lenght1)
        while trouver == bool(False):

            if(ord(mot1l[i]) <= ord(mot2l[i]) ):
                trouver = bool(True)
                resultat = str(mot1)
            elif(ord(mot1l[i]) >= ord(mot2l[i]) ):
                trouver = bool(True)
                resultat = str(mot2)
            
            i+=1
    except ValueError:
        resultat="BAD INPUT"
    except NoInputDetected:
        print("Error: NoInputDetected\n *****comparaison_mot***** \n")
        resultat="BAD INPUT"
    except NothingToCompare:
        print("It's the same string")


    return resultat


res=comparaison_mot()
print(res)
