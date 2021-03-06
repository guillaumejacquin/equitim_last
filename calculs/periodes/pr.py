from datetime import datetime
from dateutil import relativedelta

def PR1(Class):
    frequence = Class.F0

    #on transforme en date
    date_time_obj = datetime.strptime(Class.DDCI, '%Y-%m-%d')
    date_time_obj2 = datetime.strptime(Class.DPR, '%Y-%m-%d')

    #soustraction des 2 dates
    diff = abs(date_time_obj2 - date_time_obj)
    #Calcul à la louche, pour arrondir
    years = diff.days / 365
    months = diff.days / 30
    days = diff.days
    semestriels = diff.days/150
    trimestriels = diff.days / 91

    if (frequence == "jours"):
        result = int(days)

    #arrondis
    if (frequence == "mois"): #choper la fréquence et augmenter de un selon les jours
        result = int(months)
        if (months % days >= 15):
            result += 1

    if (frequence == "année"):
        result = float(years)
        print("----------")
        print(result%365)
        if (days % 365 >= 182):
            result += 1
        print(int(result))


    if (frequence == "semestre"):
        result = int(semestriels)
        if (semestriels % days >= 91):
            result += 1

    if (frequence == "trimestre"):
        result = int(trimestriels)
        if (trimestriels % days >= 45):
            result += 1

    result = abs(result)
    
    #avant derniere date 
    Class.PR1_1 = int(result -1)
    Class.PR1 = int(result)



def DPRR(Class):
    frequence = Class.F0

    date_time_obj = datetime.strptime(Class.DCF, '%Y-%m-%d')
    date_time_obj2 = datetime.strptime(Class.DDCI, '%Y-%m-%d')
    diff = date_time_obj2 - date_time_obj
    years = diff.days / 365
    months = diff.days / 30.2
    days = diff.days
    semestriels = diff.days/182
    trimestriels = diff.days / 91

   
    if (frequence == "jours"):
        result = int(days)

              
    if (frequence == "mois"):
        result = int(months)
        if (months % days >=21):
            result += 1
    if (frequence == "année"):
        result = int(years)
        if (years % days >= 182):
            result += 1

    if (frequence == "semestre"):
        result = int(semestriels)
        if (semestriels % days >= 91):
            result += 1

    if (frequence == "trimestre"):
        result = int(trimestriels)
        if (trimestriels % days >= 45):
            result += 1

    #derniere periode
    result = abs(result)

    #avant derniere periode
    avantderniereperiode = abs(result -1)

    # avantderniereperiode = frequence + " " + str(avantderniereperiode)

    Class.DPRR = int(result)
    Class.GCE = float(Class.DPRR) * float(Class.CPN)
    Class.GCE = float(Class.GCE)

    Class.ADPR = avantderniereperiode


def f1_f2(Class):
    frequence = Class.F0

    if (frequence == "jours"):
        Class.F1 = "quotidienne"
        Class.F2 = "calendaire"
    
    if (frequence == "mois"):
        Class.F1 = "mensuelle"
        Class.F2 = "écoulé"
    
    if (frequence == "année"):
        Class.F1 = "annuelle"
        Class.F2 = "écoulée"
    
    if (frequence == "semestre"):
        Class.F1 = "semestrielle"
        Class.F2 = "écoulé"

    if (frequence == "trimestre"):
        Class.F1 = "trimestrielle"
        Class.F2 = "écoulé"
