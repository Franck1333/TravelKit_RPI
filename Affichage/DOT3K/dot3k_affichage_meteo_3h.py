#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import dot3k.lcd as lcd
import time #time.sleep(valeur de temps)

#------------------------------------------------------------
# Add the root GPS dir so Python can find the modules
import sys
sys.path.append('/home/pi/TravelKit_RPI/GPS')
from Meteo_3h import main_meteo_3h
from Meteo_3h import confirme_erreur_ville
from Recuperation_Determination import lecture_serie
#------------------------------------------------------------
import pyowm

def recuperation_3h_dot3k():
    global will_pluie
    global will_soleil
    global will_snow
    
    will_pluie,will_soleil,will_snow = main_meteo_3h()    

def pluie_3h():

    #--------------------------------
    #Prochainement de la Pluie ?
    lcd.clear()                                 #Nettoyage de la Zone Affichable
    lcd.set_cursor_position(0,0)                #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Pluie dans 3H?")                 #Affichage du String entre guillemet

    if will_pluie == True :                             #Si il y a de la pluie alors...
        lcd.set_cursor_position(0,1)
        lcd.write("Pluie prevue")                       #On affirme cela par un message

    elif will_pluie == False :                          #Sinon...
        lcd.set_cursor_position(0,1)                    #Positionnement du Curseur à la colonne 0 et ligne 1
        lcd.write("Aucune pluie prevue")                #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable
    #--------------------------------
def soleil_3h():
    #Prochainement du Soleil ?

    #--------------------------------
    lcd.clear()                                     #Nettoyage de la Zone Affichable
    lcd.set_cursor_position(0,0)                    #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Soleil dans 3H?")                    #Affichage du String entre guillemet

    if will_soleil == True :                        #Si il y a de la pluie alors...
        lcd.set_cursor_position(0,1)
        lcd.write("Soleil prevue")                  #On affirme cela par un message

    elif will_soleil == False :                     #Sinon...
        lcd.set_cursor_position(0,1)                #Positionnement du Curseur à la colonne 0 et ligne 1
        lcd.write("Aucune Soleil prevue")           #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable
    #--------------------------------

def neige_3h():
    #Prochainement de la Neige ?

    #--------------------------------
    lcd.clear()                                         #Nettoyage de la Zone Affichable
    lcd.set_cursor_position(0,0)                        #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Neige dans 3H?")                         #Affichage du String entre guillemet

    if will_snow == True :                              #Si il y a de la pluie alors...
        lcd.set_cursor_position(0,1)
        lcd.write("Neige prevue")                       #On affirme cela par un message

    elif will_snow == False :                           #Sinon...
        lcd.set_cursor_position(0,1)                    #Positionnement du Curseur à la colonne 0 et ligne 1
        lcd.write("Aucune Neige prevue")                #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable
    #--------------------------------
def timer_affichage_3h():
    #----------TIMER----------
    pluie_3h()                  #Affichage de l'estimation de Pluie (Y/N)
    time.sleep(3)                       #Timer de 5 Secondes pour laisser le temps à l'utilisateur de voir les informations avant de passer à la prochaine fonction
    soleil_3h()                 #Affichage de l'estimation de Soleil (Y/N)
    time.sleep(3)
    neige_3h()                  #Affichage de l'estimation de Neige (Y/N)
    #----------TIMER----------

if __name__ == "__main__":
    try:                                                                #---!!!GESTION DES ERREURS!!!---
        recuperation_3h_dot3k()    #Fonction de Recuperation des données précedement obtenues via l'API Météo
        timer_affichage_3h()       #Lancement des Affichages des informations avec un Timer définit
        pass                                                                            #Si le tout fonctionne alors on continue
    
    except TypeError:                                                                   #Si il y a eu une erreur de TYPE de variables alors...
        lcd.clear()
        lcd.set_cursor_position(0,0)
        lcd.write("Signal GPS perdu")                                                   #On affiche un Message sur le DOT3K
        lcd.set_cursor_position(0,1)
        lcd.write("TypeError")                                                          #On affiche le code erreur
        print("Le signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: TypeError")                                                 #Affichage Code Erreur Correspondant

    except pyowm.exceptions.not_found_error.NotFoundError:                              #Si la recherche n'a donné aucun résultat alors
        lcd.clear()
        lcd.set_cursor_position(0,0)
        lcd.write("Ville non-trouve")                                                   #On affiche un Message sur le DOT3K
        lcd.set_cursor_position(0,2)
        lcd.write("not_found_error")                                                    #On affiche le code erreur
        confirme_erreur_ville()                                                         #On met un booléan a la valeur True
        print("La ville ou vous situez n'a pas ete trouver!")          #Et on affiche un message dans la console
        print("Code Erreur: pyowm.exceptions.not_found_error.NotFoundError")            #Affichage Code Erreur Correspondant

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

