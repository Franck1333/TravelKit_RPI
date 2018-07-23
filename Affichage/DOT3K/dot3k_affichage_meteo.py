#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import dot3k.lcd as lcd
import time #time.sleep(valeur de temps)
#from dot3k.menu import MenuOption,Menu

#------------------------------------------------------------
# Add the root GPS dir so Python can find the modules
import sys
sys.path.append('/home/pi/Desktop/TravelKit_RPI/GPS')
from Recuperation_Determination import meteo
from Meteo import main_meteo
#------------------------------------------------------------
import pyowm

print("""
Ce fichier va afficher sur le DOT3K, la temperature ambiante de la ZONE.
""")
#-----------------------------------------------------------------------------------------------------------------------------------------------
def recuperation_meteo_dot3k():

    global climat_min
    global climat_max
    global climat_now
    global vitesse_du_vent
    global status_climat
    global volume_de_neige
    global volume_de_pluie
    global couverture_de_nuage
    global pourcentage_humidite
    global lever_du_soleil
    global coucher_du_soleil

    climat_min,climat_max,climat_now,vitesse_du_vent,status_climat,volume_de_neige,volume_de_pluie,couverture_de_nuage,pourcentage_humidite,lever_du_soleil,coucher_du_soleil = main_meteo()
#-----------------------------------------------------------------------------------------------------------------------------------------------
    
def temperatures():
#--------------------------------
    #TEMPERATURE AMBIANTE
    lcd.clear()                             #Nettoyage de la Zone Affichable
    lcd.set_cursor_position(0,0)            #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Temp Ambiante:")             #Affichage du String entre guillemet

    
    lcd.set_cursor_position(0,1)            #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(str(climat_now))              #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable
#--------------------------------
    time.sleep(5)
#--------------------------------
    #TEMPERATURE MIN & MAX

    lcd.clear()                         #Nettoyage de la Zone Affichable
    lcd.set_cursor_position(0,0)        #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Temp MIN/MAX:")          #Affichage du String entre guillemet

    
    lcd.set_cursor_position(0,1)    #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(str(climat_min))      #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable

    lcd.set_cursor_position(0,2)    #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(str(climat_max))      #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable
#--------------------------------

def Vitesse_du_vent():
    #Vitesse du Vent
    #--------------------------------
    lcd.clear()                                 #Nettoyage de la Zone Affichable
    lcd.set_cursor_position(0,0)                #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Vitesse Vent m/s")               #Affichage du String entre guillemet

    lcd.set_cursor_position(0,1)                #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(str(vitesse_du_vent))             #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable    
    #--------------------------------

def condition_climatique():
    #Status de la Météo Actuel
    #--------------------------------
    lcd.clear()                                 #Nettoyage de la Zone Affichable
    lcd.set_cursor_position(0,0)                #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Condition Meteo")                #Affichage du String entre guillemet

    lcd.set_cursor_position(0,1)            #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write("Actuel:")                    #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable

    lcd.set_cursor_position(0,2)            #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(status_climat)                #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable    
    #--------------------------------

def Volumes():
    #Volume de Neige (en m² ?)
    #--------------------------------
    lcd.clear()                                     #Nettoyage de la Zone Affichable
    lcd.set_cursor_position(0,0)                    #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Volumes Neige/Pluie")                #Affichage du String entre guillemet

    lcd.set_cursor_position(0,1)            #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(volume_de_neige)              #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable

    lcd.set_cursor_position(0,2)         #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(str(volume_de_pluie))      #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable    
    #--------------------------------
def Taux_de_Nuage():
    #Taux de Nuages présent dans le ciel
    #--------------------------------
    lcd.clear()                                 #Nettoyage de la Zone Affichable
    lcd.set_cursor_position(0,0)                #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Taux Nuage")                     #Affichage du String entre guillemet

    lcd.set_cursor_position(0,1)                #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(str(couverture_de_nuage))         #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable  
    #--------------------------------

def Taux_Humidite():
    #Taux d'Humidité présent dans l'Environnement actuel
    #--------------------------------
    lcd.clear()                                 #Nettoyage de la Zone Affichable
    lcd.set_cursor_position(0,0)                #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Taux d'Humidite")                #Affichage du String entre guillemet

    lcd.set_cursor_position(0,1)                #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(str(pourcentage_humidite))        #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable  
    #--------------------------------
    
def timer_affichage():
    #----------TIMER----------
    temperatures()          #Affichage des Temperatures sur le DOT3K
    time.sleep(5)                   #Timer de 5 Secondes pour laisser le temps a l'utilisateur de voir les informations avant de passer à la prochaine fonction
    Vitesse_du_vent()       #Affichage de la Vitesse du Vent en Mètre par Seconde
    time.sleep(5)
    condition_climatique()  #Affichage du Status de la Météo au moment de la Requête
    time.sleep(5)
    Volumes()               #Affichage du Volume de Neige et de Pluie tombé au sol
    time.sleep(3)
    Taux_de_Nuage()         #Affichage du Taux de Nuage présent dans le ciel
    time.sleep(5)
    Taux_Humidite()         #Affichage du Taux d'Humidité présent dans l'Environnement lors de la Requête
    time.sleep(5)
    #----------TIMER----------

if __name__ == "__main__":
    try:                                                                 #---!!!GESTION DES ERREURS!!!--
        recuperation_meteo_dot3k()      #Fonction de Recuperation des données précedement obtenues via l'API Météo
        timer_affichage()               #Lancement des Affichages des informations avec un Timer définit
        pass

    except TypeError:                                                                   #Si il y a eu une erreur de TYPE de variables alors...
        lcd.clear()
        lcd.set_cursor_position(0,0)
        lcd.write("Signal GPS perdu")                                                   #On affiche un Message sur le DOT3K

        lcd.set_cursor_position(0,1)
        lcd.write("Deplacez-Vous!")

        lcd.set_cursor_position(0,2)
        lcd.write("TypeError")                                                          #On affiche le code erreur
        print("Le signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: TypeError")

    except AssertionError:                                                              #Si il y a eu une erreur de TYPE de variables alors...
        lcd.clear()
        lcd.set_cursor_position(0,0)
        lcd.write("Signal GPS perdu")                                                   #On affiche un Message sur le DOT3K

        lcd.set_cursor_position(0,1)
        lcd.write("Deplacez-Vous!")
        
        lcd.set_cursor_position(0,2)
        lcd.write("AssertionError")
        print("Le Signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: AssertionError")
                                                                       
    except:
        lcd.clear()
        lcd.set_cursor_position(0,0)
        lcd.write("Redemarrez le GPS")                                                  #On affiche un Message sur le DOT3K
        lcd.set_cursor_position(0,2)
        lcd.write("Unknow error")                                                       #On affiche le code erreur
        print("Il est necessaire de Redemarrez le GPS!")                                #On affiche ce message dans la console
        print("Code Erreur: Aucun")

                                                                         #---!!!GESTION DES ERREURS!!!---
