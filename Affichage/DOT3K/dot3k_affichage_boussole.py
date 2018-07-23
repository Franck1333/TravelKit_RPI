#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import dot3k.lcd as lcd
import time #time.sleep(valeur de temps)

#------------------------------------------------------------
# Add the root GPS dir so Python can find the modules
import sys
sys.path.append('/home/pi/Desktop/TravelKit_RPI/GPS')
from Boussole import boussole
from Recuperation_Determination import lecture_serie
#------------------------------------------------------------

def recuperation_boussole_dot3k():
    #lecture_serie()
    
    global round_retourne_latitude
    global dir_Latitude_Hemisphere
    global round_retourne_longitude
    global dir_Longitude_Hemisphere

    round_retourne_latitude,dir_Latitude_Hemisphere,round_retourne_longitude,dir_Longitude_Hemisphere = boussole()

def affichage_de_la_boussole_dot3k_1():
    #--------------------------------
    #BOUSSOLE 1/2
    lcd.clear()                             #Nettoyage de la Zone Affichable
    lcd.set_cursor_position(0,0)            #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("BOUSSOLE 1/2")               #Affichage du String entre guillemet

    
    lcd.set_cursor_position(0,1)                        #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(str(round_retourne_latitude))             #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable

    lcd.set_cursor_position(0,2)                        #Positionnement du Curseur à la colonne 0 et ligne 2
    lcd.write(dir_Latitude_Hemisphere)                  #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable
    #--------------------------------
    
def affichage_de_la_boussole_dot3k_2():    
    #--------------------------------
    #BOUSSOLE 2/2
    lcd.clear()                             #Nettoyage de la Zone Affichable
    lcd.set_cursor_position(0,0)            #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("BOUSSOLE 2/2")               #Affichage du String entre guillemet

    
    lcd.set_cursor_position(0,1)                        #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(str(round_retourne_longitude))            #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable

    lcd.set_cursor_position(0,2)                        #Positionnement du Curseur à la colonne 0 et ligne 2
    lcd.write(dir_Longitude_Hemisphere)                 #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable
    #--------------------------------

def timer_boussole_dot3k(): #Timer permettant d'afficher rapidement les informations sur le DOT3K
    #La Méthode lcd.write n'autorise pas de mettre plus d'un paramètre pour l'utiliser donc impossible de faire toute les informations sur la même page , donc j'en fait deux , pour les quatres informations obtenues.
    
    affichage_de_la_boussole_dot3k_1() #Partie Une
    time.sleep(2)                           #Timer Rapide
    affichage_de_la_boussole_dot3k_2() #Partie Deux
    time.sleep(2)
    affichage_de_la_boussole_dot3k_1()
    time.sleep(2)
    affichage_de_la_boussole_dot3k_2()
    time.sleep(2)
    affichage_de_la_boussole_dot3k_1()
    time.sleep(2)
    affichage_de_la_boussole_dot3k_2()
    time.sleep(2)
    affichage_de_la_boussole_dot3k_1()
    time.sleep(2)
    affichage_de_la_boussole_dot3k_2()
    
if __name__ == "__main__":
    try:                                                                 #---!!!GESTION DES ERREURS!!!---
        recuperation_boussole_dot3k()      #Fonction de Recuperation des données précedement obtenues via l'API Météo
        timer_boussole_dot3k()           #Lancement des Affichages des informations avec un Timer définit
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
        
