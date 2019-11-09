import os
import sys

"""Je suis ligoté sur les rails en gare d’Arras. Écrire un programme qui affiche un
tableau me permettant de connaître l’heure à laquelle je serai déchiqueté par le train parti
de la gare du Nord à 9h (il y a 170 km entre la gare du Nord et Arras). Le tableau prédira
les différentes heures possibles pour toutes les vitesses de 100 km/h à 300 km/h, par pas
de 10 km/h, les résultats étant arrondis à la minute inférieure.
Écrire une procédure tchacatchac qui reçoit la vitesse du train et qui affiche l’heure du
drame.
Écrire le programme principal qui affiche le tableau demandé."""

class NegativeInput(Exception):
    """Negative Integer in input is not allowed"""
class TooMuchArgs(Exception):
    """Too much args in line of input file"""

def tchacatchac(trainSpeed,dist): ###Create your custom function here
    departure_hour=9
    crash_time=(dist/trainSpeed)*60
    death_hour=int((crash_time//60))+departure_hour
    death_minute = round(crash_time%60)
    if death_minute < 10:
        return str(death_hour)+"h0" + str(death_minute)
    else :
        return str(death_hour)+"h"+str(death_minute)

def deathHourList(dist,minSpeed,maxSpeed,step):
    dist,minSpeed,maxSpeed,step = int(dist),int(minSpeed),int(maxSpeed),int(step)
    if dist<=0 or minSpeed<=0 or maxSpeed<=0 or step<=0:
        raise NegativeInput
    tab_string = "   {}(en km/h)   |   {}   "
    print(tab_string.format("Vitesse","Heure"))
    for i in range(minSpeed,maxSpeed,step):
        print(tab_string.format(i,tchacatchac(i,dist)))

def main(line):
    try:
        if len(line.split(";"))!=4:###Change number of args need on one line
            raise TooMuchArgs
        else:
            dist,minSpeed,maxSpeed,step = line.split(";")
            result=deathHourList(dist,minSpeed,maxSpeed,step) ####Change function name and args
            if result == None:
                return
            else:
                print(result)
    except TooMuchArgs:
        print("BAD INPUT - Too much args for this programme")
    except ZeroDivisionError:
        print("BAD INPUT - Zero in a division has been found")
    except ValueError:
        print("BAD INPUT - Float or string detected")
    except NegativeInput:
        print("BAD INPUT - Negative train speed")

if __name__=="__main__":
    try:
        inputFile=open(sys.argv[1],"r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND "+sys.argv[1] )
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")

