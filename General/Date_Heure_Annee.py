#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides: https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-python/28189525

from datetime import datetime

def temps_actuel_precis():

    currentSecond= datetime.now().second            #Obtention de la Seconde Actuel
    currentMinute = datetime.now().minute           #Obtention de la Minute Actuel
    currentHour = datetime.now().hour               #Obtention de l'Heure Actuel

    currentDay = datetime.now().day                 #Obtention du Jour Actuel
    currentMonth = datetime.now().month             #Obtention du Mois Actuel
    currentYear = datetime.now().year               #Obtention de l'AnnÃ©e en cours...

    print("Il est:" , currentHour,":",currentMinute,":",currentSecond)  #Affichage de l'Heure,Minute,Seconde
    print("Nous sommes le:",currentDay,"/",currentMonth)                #Affichage de la Date "Jour,Mois"
    print("Nous sommes en:",currentYear)                                #Affichage de l'AnnÃ©e en cours....

    return currentHour,currentMinute,currentSecond,currentDay,currentMonth,currentYear  #Toute les donnÃ©es obtenues sont retournÃ© dans le cadre d'une future utilisations de celles-ci


if __name__ == "__main__":
    temps_actuel_precis()                                   #FonctionnalitÃ© permettant d'Obtenir le Temps SystÃ¨me Actuel
