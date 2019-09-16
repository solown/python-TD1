


def comparaison_mot():

        i=int(0)
        trouver=bool("FALSE")
        resultat=""
        mot1=(str(input("Entrer un mot: ")))
        mot2=(str(input("Entrer un mot: ")))
        lenght1=len(mot1)
        lenght2=len(mot2)
        if lenght1>lenght2:
            max=int(lenght2)-1
        else:
            max=int(lenght1) -1
        print(max)
        while trouver == bool("FALSE") and int(i)<int(max):
            print(i)
            if(ord(mot1[i]) > ord(mot2[i])):
                trouver = bool("TRUE")
                resultat = mot2
            elif(ord(mot2[i]) > ord(mot1[i])):
                trouver = bool("TRUE")
                resultat = mot1

            i+=1

        return resultat

res=comparaison_mot()
print(res)
