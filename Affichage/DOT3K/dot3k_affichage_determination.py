#!/usr/bin/env python
# -*- coding: cp1252 -*-

import dot3k.lcd as lcd
import time

#------------------------------------------------------------
# Add the root GPS dir so Python can find the modules
import sys
sys.path.append('/home/pi/TravelKit_RPI/GPS')
from Recuperation_Determination import recup_affichage
from Recuperation_Determination import determine_less
from Recuperation_Determination import parse_GPRMC
#------------------------------------------------------------

print("""
Ce fichier va afficher sur le DOT3K, la localisation determine de la ZONE.
""")

def determination_dot3k():

    recup_affichage()               #Demarrage du fichier python Recuperation_Determination.py 
    global ville                    #Déclaration de la variable GLOBAL 'ville'
    ville = determine_less()        #L'information dtermine par un autre fichier python est stocker dans la variable pour être utiliser apès

    #Using the 'lcd.write' way
    lcd.clear()                     #Nettoyage de la Zone Affichable
    
    lcd.set_cursor_position(0,0)    #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Nous sommes ici:")          #Affichage du String entre guillemet
    
    lcd.set_cursor_position(0,1)    #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(ville)            #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable
    #return lcd.write(ville)            #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable

if __name__ == "__main__":
    try:                                                                #---!!!GESTION DES ERREURS!!!---
        determination_dot3k() #Fonction Affichage sur le DOT3K
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
