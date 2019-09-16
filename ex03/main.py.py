


def comparaison_mot():

        i=int(0)
        trouver=bool("FALSE")
        resultat=""
        mot1=(str(input("Entrer un mot: ")))
        mot2=(str(input("Entrer un mot: ")))
        lenght1=len(mot1)
        lenght2=len(mot2)
        if lenght1>lenght2:
            max=int(lenght1) + 1
        else:
            max=int(lenght2) + 1
        print(max)
        while((trouver == "FALSE") and (i < max)):
            print(i)
            if(mot1[i] < mot2[i]):
                trouver = "TRUE"
                resultat = mot2
            elif(mot2[i] < mot1[i]):
                trouver = "TRUE"
                resultat = mot1
            else:
                i+=i
        print(mot1)
        print(mot2)
        return resultat

res=comparaison_mot()
print(res)
