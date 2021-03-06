#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides :
#https://gist.github.com/Lauszus/5785023
#https://raspberry-pi.developpez.com/cours-tutoriels/projets-rpi-zero/traceur-gps/
#https://stackoverflow.com/questions/20169467/how-to-convert-from-longitude-and-latitude-to-country-or-city
###https://github.com/googlemaps/google-maps-services-python
#AIDES: https://github.com/geopy/geopy
#AIDES: https://pypi.org/project/geopy/
#AIDES: https://geopy.readthedocs.io/en/stable/index.html?highlight=reverse

import serial
import time
import os
import sys
from urllib2 import urlopen
#from urllib.request import urlopen
import json

#---REVERSE_GEOCODING_GEOPY---
import geopy.geocoders                  #--> sudo pip install geopy 
from geopy.geocoders import Nominatim   #Nominatim Service
#---REVERSE_GEOCODING_GEOPY---

#---
#Cette blibliothèque permet de travailler avec du contenue contenant des accents
import unidecode #--> sudo pip install unicode

#unaccented_location = unidecode.unidecode(location.address)
#---

import datetime

#import dot3k.lcd as lcd
#import dot3k.backlight as backlight

from nettoyage_du_cache import clear_cache

import unicodedata #Cette blibliothèque permet de travailler avec du contenue contenant des accents

#---DEBUT---Variables Par Défault---
Validite = None
Decimal_latitude = None
Decimal_longitude = None
#---FIN---Variables Par Défault---

ser = serial.Serial('/dev/ttyACM0',4800,timeout=1) # Open Serial port Configure le Recepteur G.P.S

#Recuparation des informations de la Trame GPRMC contenant les coordonnees GPS principales
# Helper function to take HHMM.SS, Hemisphere and make it decimal:
#-------------------------------
def degrees_to_decimal(data, hemisphere):
    try:
        decimalPointPosition = data.index('.')
        degrees = float(data[:decimalPointPosition-2])
        minutes = float(data[decimalPointPosition-2:])/60
        output = degrees + minutes
        if hemisphere is 'N' or hemisphere is 'E':
            return output
        if hemisphere is 'S' or hemisphere is 'W':
            return -output
    except:
        return ""
#-------------------------------    
# Helper function to take a $GPRMC sentence, and turn it into a Python dictionary.
def parse_GPRMC(data):    
    data = data.split(',')
    dict = {
            'Temps_Capture': data[1],
            'Validite': data[2],
            'Latitude': data[3],
            'Latitude_Hemisphere' : data[4],
            'Longitude' : data[5],
            'Longitude_Hemisphere' : data[6],
            'Vitesse': data[7],
            #'Angle': data[8],
            #'fix_date': data[9],
            #'variation': data[10],
            #'variation_e_w' : data[11],
            'Checksum' : data[12]
    }
    dict['decimal_latitude'] = degrees_to_decimal(dict['Latitude'], dict['Latitude_Hemisphere'])
    dict['decimal_longitude'] = degrees_to_decimal(dict['Longitude'], dict['Longitude_Hemisphere'])

    global Validite
    global Latitude
    global Longitude

    global Latitude_Hemisphere
    global Longitude_Hemisphere

    global Decimal_latitude    #VARIABLE GLOBAL CONVERTIS LATITUDE
    global Decimal_longitude   #VARIABLE GLOBAL CONVERTIS LONGITUDE

    Validite = dict['Validite']
    Latitude = dict['Latitude']
    Longitude = dict['Longitude']

    Latitude_Hemisphere = dict['Latitude_Hemisphere']
    Longitude_Hemisphere = dict['Longitude_Hemisphere']    
    
    Decimal_latitude = dict['decimal_latitude']   #DICTIONNAIRE VARIABLE LATITUDE CONVERTIS
    Decimal_longitude = dict['decimal_longitude'] #DICTIONNAIRE VARIABLE LONGITUDE CONVERTIS

    #print("La Direction du CAP:",Decimal_latitude,Latitude_Hemisphere,'-',Decimal_longitude,Longitude_Hemisphere ) #TEST - DEBUG
      
    return Decimal_latitude,Decimal_longitude,Validite,Latitude_Hemisphere,Longitude_Hemisphere #RETOURNE LES VARIABLES CONVERTIS LATITUDE,LONGITUDE
    
   #return dict #Retourne le dictionnaire principale
#-------------------------------

#-------------------------------
def etat_trame(): #Verification de la conformite de la Trame NMEA reçu

    #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
    #-- DEBUT -- Heure,Minute,Seconde
    tt = time.time()
    system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
    #print (system_time)
    #-- FIN -- Heure,Minute,Seconde

    #Zone de TEST --DEBUT--
    #Validite_valid = isinstance(Validite,str) #<-- TEST
    Decimal_latitude_valid = isinstance(Decimal_latitude,float) #<-- TEST
    Decimal_longitude_valid = isinstance(Decimal_longitude,float) #<-- TEST
    #Zone de TEST --FIN--


    #Cette fonction va verifie la conformite de la Trame NMEA reçu par le Stick GPS et relance le Menu Principal si une erreur est detecte en testant la variable 'Validite'
    if Validite == 'A' and Decimal_latitude_valid == True and Decimal_longitude_valid == True :   #Si la variable est valide alors...

        #Lumière -- DEBUT --
        #print("Affichage VERT")
        #backlight.rgb(0, 255, 0)    #Paramètre RGB Lumiere
        #Lumière -- FIN --

        #PARAMETRAGE BARGRAPH --DEBUT--
        #for i in range(13):
        #    backlight.set_graph(i / 13.0)
        #time.sleep(0.05)
        #PARAMETRAGE BARGRAPH --FIN--
        
        print(Validite)                 #Affichage de la Variable "Validite" dans la console
        print("Trame NMEA Valide")      #Affichage du String entre guillemet
        print("Signal GPS Obtenue")     #Affichage du String entre guillemet
        print (system_time)
        pass #<--   
    

    elif Validite == None or Decimal_latitude == None or Decimal_longitude == None  : #Sinon alors...

        #Lumière -- DEBUT --
        #print("Affichage JAUNE")
        #backlight.rgb(255, 255, 0)    #Paramètre RGB Lumiere
        #Lumière -- FIN --

        print("elif Variables == None")
        print("Variables Non Utilisable")                           #Affichage du String entre guillemet
        print("Signal GPS Perdue")                                  #Affichage du String entre guillemet
        print("Redemarrage en cours du Programme MENU PRINCIPAL")
        print (system_time)

        #DOT3K CHECK ERROR DISPLAY --DEBUT--
        #lcd.clear()                         #Nettoyage de la Zone Affichable

        #lcd.set_cursor_position(0,0)        #Positionnement du Curseur à la colonne 0 et ligne 0
        #lcd.write("CHECKING VAR")           #Affichage du String entre guillemet
        
        #lcd.set_cursor_position(0,1)        #Positionnement du Curseur à la colonne 0 et ligne 1
        #lcd.write(system_time)              #Affichage du String entre guillemet

        #lcd.set_cursor_position(0,2)        #Positionnement du Curseur à la colonne 0 et ligne 1
        #lcd.write("Restart!!!")             #Affichage du String entre guillemet
        #DOT3K CHECK ERROR DISPLAY --FIN--
        
        #Execution du fichier MENU 'dot3k_automenu.py'
        time.sleep(5)
        clear_cache()                       #Nettoyage des Fichiers caches PYTHON
        #os.system('sudo python /home/pi/GPS_Display/Mon_Travail/dot3k_automenu.py') #Redemarre le Menu et les fonctions dans le Menu avec <--

        exit

    elif Decimal_latitude_valid == False : #Sinon alors...

        #Lumière -- DEBUT --
        #print("Affichage ROUGE")
        #backlight.rgb(255, 0, 0)    #Paramètre RGB Lumiere
        #Lumière -- FIN --

        print("elif Decimal_latitude_valid == False ")
        print("Variables Non Utilisable")                           #Affichage du String entre guillemet
        print("Signal GPS Perdue")                                  #Affichage du String entre guillemet
        print("Redemarrage en cours du Programme MENU PRINCIPAL")
        print (system_time)

        #DOT3K CHECK ERROR DISPLAY --DEBUT--
        #lcd.clear()                         #Nettoyage de la Zone Affichable

        #lcd.set_cursor_position(0,0)        #Positionnement du Curseur à la colonne 0 et ligne 0
        #lcd.write("CHECKING VAR")           #Affichage du String entre guillemet
        
        #lcd.set_cursor_position(0,1)        #Positionnement du Curseur à la colonne 0 et ligne 1
        #lcd.write(system_time)              #Affichage du String entre guillemet

        #lcd.set_cursor_position(0,2)        #Positionnement du Curseur à la colonne 0 et ligne 1
        #lcd.write("Restart!!!")             #Affichage du String entre guillemet
        #DOT3K CHECK ERROR DISPLAY --FIN--
        
        #Execution du fichier MENU 'dot3k_automenu.py'
        time.sleep(5)
        clear_cache()                       #Nettoyage des Fichiers caches PYTHON
        #os.system('sudo python /home/pi/GPS_Display/Mon_Travail/dot3k_automenu.py') #Redemarre le Menu et les fonctions dans le Menu avec <--
        exit
        
    elif Decimal_longitude_valid == False  : #Sinon alors...
        
        #Lumière -- DEBUT --
        #print("Affichage ROUGE")
        #backlight.rgb(255, 0, 0)    #Paramètre RGB Lumiere
        #Lumière -- FIN --

        print("elif Decimal_longitude_valid == False ")
        print("Variables Non Utilisable")                           #Affichage du String entre guillemet
        print("Signal GPS Perdue")                                  #Affichage du String entre guillemet
        print("Redemarrage en cours du Programme MENU PRINCIPAL")
        print (system_time)

        #DOT3K CHECK ERROR DISPLAY --DEBUT--
        #lcd.clear()                         #Nettoyage de la Zone Affichable

        #lcd.set_cursor_position(0,0)        #Positionnement du Curseur à la colonne 0 et ligne 0
        #lcd.write("CHECKING VAR")           #Affichage du String entre guillemet
        
        #lcd.set_cursor_position(0,1)        #Positionnement du Curseur à la colonne 0 et ligne 1
        #lcd.write(system_time)              #Affichage du String entre guillemet

        #lcd.set_cursor_position(0,2)        #Positionnement du Curseur à la colonne 0 et ligne 1
        #lcd.write("Restart!!!")             #Affichage du String entre guillemet
        #DOT3K CHECK ERROR DISPLAY --FIN--
        
        #Execution du fichier MENU 'dot3k_automenu.py'
        time.sleep(5)
        clear_cache()                       #Nettoyage des Fichiers caches PYTHON
        #os.system('sudo python /home/pi/GPS_Display/Mon_Travail/dot3k_automenu.py') #Redemarre le Menu et les fonctions dans le Menu avec <--

        exit 
    else :                                                  #Sinon alors...
        
        #Lumière -- DEBUT --
        #print("Affichage BLANC + JAUNE")
        #backlight.rgb(255, 255, 245)    #Paramètre RGB Lumiere
        #Lumière -- FIN --

        print("else conditions")
        print(Validite)                                     #Affichage de la Variable "Validite" dans la console
        print("Trame NMEA NON VALIDE")                      #Affichage du String entre guillemet
        print("Signal GPS Perdue")                          #Affichage du String entre guillemet
        print("Redemarrage en cours du Programme MENU PRINCIPAL")
        print (system_time)

        #DOT3K CHECK ERROR DISPLAY --DEBUT--
        #lcd.clear()                         #Nettoyage de la Zone Affichable

        #lcd.set_cursor_position(0,0)        #Positionnement du Curseur à la colonne 0 et ligne 0
        #lcd.write(system_time)              #Affichage du String entre guillemet
        
        #lcd.set_cursor_position(0,1)        #Positionnement du Curseur à la colonne 0 et ligne 1
        #lcd.write("Signal GPS Perdue")      #Affichage du String entre guillemet

        #lcd.set_cursor_position(0,2)        #Positionnement du Curseur à la colonne 0 et ligne 1
        #lcd.write("Restart en cours...")    #Affichage du String entre guillemet        
        #DOT3K CHECK ERROR DISPLAY --FIN--

        #Execution du fichier MENU 'dot3k_automenu.py'
        time.sleep(13)
        clear_cache()                       #Nettoyage des Fichiers caches PYTHON
        #os.system('sudo python /home/pi/GPS_Display/Mon_Travail/dot3k_automenu.py') #Redemarre le Menu et les fonctions dans le Menu avec <--
        exit

#-------------------------------

#-------------------------------
def retourne_latitude():
    
    Retourne_latitude = Decimal_latitude #Initialisation de la nouvelle variable à la Latitude pour le partage avec un autre fichier python
    
    return Retourne_latitude #Retourne la nouvelle Valeur LATITUDE   
#-------------------------------
#-------------------------------
def retourne_longitude():
        
    Retourne_longitude = Decimal_longitude #Initialisation de la nouvelle variable à la Longitude pour le partage avec un autre fichier python

    return Retourne_longitude #Retourne la nouvelle Valeur LONGITUDE
#-------------------------------
#-------------------------------
def retourne_Latitude_Hemisphere():

    Retourne_Latitude_Hemisphere = Latitude_Hemisphere      #Initialisation de la nouvelle variable à la Longitude pour le partage avec un autre fichier python

    return Retourne_Latitude_Hemisphere                     #Retourne la nouvelle Valeur LATITUDE_HEMISPHERE

#-------------------------------
#-------------------------------
def retourne_Longitude_Hemisphere():

    Retourne_Longitude_Hemisphere = Longitude_Hemisphere    #Initialisation de la nouvelle variable à la Longitude pour le partage avec un autre fichier python

    return Retourne_Longitude_Hemisphere                    #Retourne la nouvelle Valeur LONGITUDE_HEMISPHERE
#-------------------------------
def determine():
   
    geolocator = Nominatim(user_agent="GPS-SWAGG")                          #Utilisation des Services de Reverse-Geocoding de Nominatim, https://nominatim.openstreetmap.org/reverse.php?format=html

    coordonees_GPS = str(Decimal_latitude) +","+ str(Decimal_longitude)

    print(coordonees_GPS)

    location = geolocator.reverse(coordonees_GPS)      #Envoie aux Services de Nominatim les coordonées GPS et reception de la Réponse

    unaccented_location = unidecode.unidecode(location.address)             #On Retire les Accents de la Réponse de l'API
    print("\n")                                                             #Saut de ligne
    print(unaccented_location)                                              #Affichage de la Réponse (sans accents)
    print("\n")                                                             #Saut de Ligne
    #Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union

    print((location.latitude, location.longitude))                          #Affichage des coordonées du Lieu indiqué
    #(52.5094982, 13.3765983)

    print("\n")
    #print(location.raw)

    Ville =         location.raw['address']['town']                         #Enregistrement de la Ville depuis la version "RAW" du Service Nominatim
    Numero_Maison = location.raw['address']['house_number']                 #Enregistrement du Numéro de Rue depuis la version "RAW" du Service Nominatim
    Rue =           location.raw['address']['road']                         #Enregistrement de la Rue depuis la version "RAW" du Service Nominatim
    Code_Postal =   location.raw['address']['postcode']                     #Enregistrement du Code Postal depuis la version "RAW" du Service Nominatim
    Pays =          location.raw['address']['country']                      #Enregistrement du Pays depuis la version "RAW" du Service Nominatim

    print(Ville)                                                            #Affichage de la Ville
    print(Numero_Maison)                                                    #Affichage du Numéro de Positionnement dans la Rue
    print(Rue)                                                              #Affichage du Nom de la Rue
    print(Code_Postal)                                                      #Affichage du Code Postal
    print(Pays)                                                             #Affichage du Pays
    #{'place_id': '654513', 'osm_type': 'node', ...}                        #Exemple du format des données reçu enregistrer dans "location.raw"
    resultat_Ville = Ville
    return resultat_Ville #RETOURNE LE STRING DE LA LOCALISATION DETERMINE    
    #---------------------------------------------
    #gmaps = googlemaps.Client(key='AIzaSyCbcLmcGDUQlhvZhAkdE0IUFh90rjJ7rrw') #Cle d'acces A.P.I

    #etat_trame() #Validation de la conformite de la Trame NMEA <--

    # Look up an address with reverse geocoding
    #reverse_geocode_result = gmaps.reverse_geocode((Decimal_latitude, Decimal_longitude)) #Envoie et Recuperation des Donnees

    #Accessing the needed part of the response
    #reverse_geocode_result[0] # This is a dict
    #reverse_geocode_result[0]['address_components'][3]['long_name'] # Return La Region
    #reverse_geocode_result[0]['address_components'][4]['long_name'] # Return country 
    #reverse_geocode_result[0]['address_components'][2]['long_name'] # Return sublocality
    #reverse_geocode_result[0]['address_components'][1]['long_name'] # Return route
    #reverse_geocode_result[0]['address_components'][0]['long_name'] # Return street number
    
    #print("On se trouve a :")
    #print(reverse_geocode_result) Format JSON

    #resultat_Ville = reverse_geocode_result[0]['formatted_address'] #STRING LOCALISATION DETERMINE
    #print (resultat_Ville) #JSON Parse (trie)
    
    #return resultat_Ville #RETOURNE LE STRING DE LA LOCALISATION DETERMINE
    #return reverse_geocode_result #RETOURNE LA LOCALISATION OBTENUE AU FORMAT JSON
    #---------------------------------------------
#-------------------------------

#-------------------------------
#NOUS INDICONS UNIQUEMENT LA VILLE ICI
def determine_less():
    etat_trame() #Validation de la conformite de la Trame NMEA <--
    
    geolocator = Nominatim(user_agent="GPS-SWAGG")                          #Utilisation des Services de Reverse-Geocoding de Nominatim, https://nominatim.openstreetmap.org/reverse.php?format=html

    coordonees_GPS = str(Decimal_latitude) +","+ str(Decimal_longitude)

    print(coordonees_GPS)

    location = geolocator.reverse(coordonees_GPS)      #Envoie aux Services de Nominatim les coordonées GPS et reception de la Réponse

    unaccented_location = unidecode.unidecode(location.address)             #On Retire les Accents de la Réponse de l'API
    print("\n")                                                             #Saut de ligne
    print(unaccented_location)                                              #Affichage de la Réponse (sans accents)
    print("\n")                                                             #Saut de Ligne
    #Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union

    print((location.latitude, location.longitude))                          #Affichage des coordonées du Lieu indiqué
    #(52.5094982, 13.3765983)

    print("\n")
    #print(location.raw)

    Ville =         location.raw['address']['town']                         #Enregistrement de la Ville depuis la version "RAW" du Service Nominatim
    Pays =          location.raw['address']['country']                      #Enregistrement du Pays depuis la version "RAW" du Service Nominatim

    print(Ville)                                                            #Affichage de la Ville
    print(Pays)                                                             #Affichage du Pays
    #{'place_id': '654513', 'osm_type': 'node', ...}                        #Exemple du format des données reçu enregistrer dans "location.raw"
    resultat_Ville = Ville
    return resultat_Ville #RETOURNE LE STRING DE LA LOCALISATION DETERMINE
#-------------------------------
#-------------------------------
def lecture_serie():
    line = ser.readline() #Lecture de la liason serie Ligne par Ligne

    if "$GPRMC" in line: #SELECTION DE LA LIGNE GPRMC
        gpsData = parse_GPRMC(line) #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'
    #etat_trame()
#-------------------------------
#-------------------------------
def meteo():
    line = ser.readline() #Lecture de la liason serie Ligne par Ligne

    if "$GPRMC" in line: #SELECTION DE LA LIGNE GPRMC
        gpsData = parse_GPRMC(line) #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'
    #etat_trame()
#-------------------------------
def recup_affichage():
    line = ser.readline() #Lecture de la liason serie Ligne par Ligne

    if "$GPRMC" in line: #SELECTION DE LA LIGNE GPRMC
        gpsData = parse_GPRMC(line) #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'
    #etat_trame()
#-------------------------------        

#---MAIN---
def main():
    line = ser.readline() #Lecture de la liason serie Ligne par Ligne

    if "$GPRMC" in line: #SELECTION DE LA LIGNE GPRMC
        gpsData = parse_GPRMC(line) #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'
        
        print(Decimal_latitude)  #AFFICHAGE DE LA VARIABLE CONVERTIS LATITUDE
        print(Decimal_longitude) #AFFICHAGE DE LA VARIABLE CONVERTIS LONGITUDE
        etat_trame() #Validation de la conformite de la Trame NMEA <--
        determine(); #FONCTION PERMETTANT DE DETERMINER LA LOCALISATION GRACE AU G.P.S
        #determine_less()
        
if __name__ == "__main__":
    try:                                                                #---!!!GESTION DES ERREURS!!!---
        main()
        pass
    except TypeError:
	print("Le signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: TypeError")
    except ValueError:
	print("Le signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: ValueError")
    except AssertionError:
	print("Le Signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: AssertionError")
    except:
	print("Il est necessaire de Redemarrez le GPS!")                                #On affiche ce message dans la console
        print("Code Erreur: Aucun")
                                                                         #---!!!GESTION DES ERREURS!!!---
