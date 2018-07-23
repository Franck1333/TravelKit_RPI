#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides :

import serial
import time
import os
import sys

from Recuperation_Determination import lecture_serie
from Recuperation_Determination import retourne_latitude
from Recuperation_Determination import retourne_longitude
from Recuperation_Determination import retourne_Latitude_Hemisphere
from Recuperation_Determination import retourne_Longitude_Hemisphere

from nettoyage_du_cache import clear_cache

import unicodedata #Cette blibliothèque permet de travailler avec du contenue contenant des accents

def boussole():
    lecture_serie()                                                 #Lecture/capture des informations provenant de la liason série

    round_retourne_latitude = retourne_latitude()                   #Enregistrement de la latitude dans une nouvelle variable
    round_retourne_longitude = retourne_longitude()                 #Enregistrement de la longitude dans une nouvelle variable

    round_retourne_latitude = round(round_retourne_latitude,4)      #On selectionne que 4 chiffres après la virgule pour la latitude 
    round_retourne_longitude = round(round_retourne_longitude,4)    #On selectionne que 4 chiffres après la virgule pour la longitude

    dir_Latitude_Hemisphere = retourne_Latitude_Hemisphere()        #Enregistrement de l'information de direction hemispherique de la LATITUDE dans une nouvelle variable
    dir_Longitude_Hemisphere = retourne_Longitude_Hemisphere()      #Enregistrement de l'information de direction hemispherique de la LONGITUDE dans une nouvelle variable

    print("La position actuel:",round_retourne_latitude,dir_Latitude_Hemisphere,'-',round_retourne_longitude,dir_Longitude_Hemisphere) #On Procède à l'affichage de toute les informations reçue

    #print(retourne_Latitude_Hemisphere())  #TEST - DEBUG
    #print(retourne_Longitude_Hemisphere()) #TEST - DEBUG

    return round_retourne_latitude,dir_Latitude_Hemisphere,round_retourne_longitude,dir_Longitude_Hemisphere    #Retourne toutes les valeurs obtenues

if __name__ == "__main__":
    clear_cache()   #Nettoyage des fichiers python indésirables
    #-----------------------------------
    try:                                                                #---!!!GESTION DES ERREURS (Simplifié)!!!---
        boussole()                                                                      #Programme principal de la Boussole Numérique (TEXTUELLE)
        pass                                                                            #On continue...
    except TypeError:                                                                   #Si il y a eu une erreur de TYPE de variables alors...
        print("Le signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: TypeError")                                                 #Affichage Code Erreur Correspondant
                                                                        #---!!!GESTION DES ERREURS (Simplifié)!!!---
    #-----------------------------------
