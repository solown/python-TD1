class NoInputDetected(Exception):
    pass
class NothingToCompare(Exception):
    pass

resultat=""
def comparaison_mot():

        try:
                mot1=(str(input("Entrer un mot: ")))
                mot2=(str(input("Entrer un mot: ")))

                if(mot1=="" or mot2==""):
                    raise NoInputDetected
                if(mot1 == mot2):
                    raise NothingToCompare


                i=int(0)
                trouver=False
                lenght1=len(mot1)
                lenght2=len(mot2)
                if lenght1>lenght2:
                    max=int(lenght2)
                else:
                    max=int(lenght1)

                global resultat
                while trouver == bool(False) and int(i)<int(max):

                    if(ord(mot1[i]) < ord(mot2[i])):
                        trouver = bool(True)
                        resultat = mot1
                    elif(ord(mot1[i]) > ord(mot2[i])):
                        trouver = bool(True)
                        resultat = mot2

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
