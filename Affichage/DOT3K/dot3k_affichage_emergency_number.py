#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Liste les Numéros de Téléphone d'Urgence du Monde entiers
#L'Amérique : 911
#L'Europe   : 112
#L'Asie     : 110 ou 119
#Reste du Monde : 999
#Si le continent n'est pas trouvé : 112 ou 911 ou 999

import dot3k.lcd as lcd
import time #time.sleep(valeur de temps)

#------------------------------------------------------------
# Add the root dir so Python can find the modules
import sys
sys.path.append('/home/pi/TravelKit_RPI/General')
from emergency_number import numero_urgence
#------------------------------------------------------------

def recuperation_info_emergency():
    global tel_urgence

    tel_urgence = numero_urgence()

def affichage_numero():
    #--------------------------------
    #NUMEROS D'URGENCES INTERNATIONAUX
    lcd.clear()                             #Nettoyage de la Zone Affichable
    lcd.set_cursor_position(0,0)            #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Numero Urgence:")             #Affichage du String entre guillemet

    lcd.set_cursor_position(0,1)            #Positionnement du Curseur à la colonne 0 et ligne 1
    print(tel_urgence)
    lcd.write(str(tel_urgence))              #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable
    #--------------------------------

if __name__ == "__main__":
    recuperation_info_emergency()
    affichage_numero()
