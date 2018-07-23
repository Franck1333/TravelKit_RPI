#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides: https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-python/28189525

import datetime
import time

def temps_actuel():
   
    #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
    #-- DEBUT -- Heure,Minute,Seconde
    tt = time.time()
    system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
    print ("Voici l'heure:",system_time)
    return system_time
    #-- FIN -- Heure,Minute,Seconde

if __name__ == "__main__":
    temps_actuel()                                   #FonctionnalitÃ© permettant d'Obtenir le Temps SystÃ¨me Actuel
