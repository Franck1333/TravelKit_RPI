#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial
import time #time.sleep(valeur de temps)
import os
import sys

def ouvrir_nettoyage_cache():
    print("\n")
    #fichier permettant le Nettoyage des Fichiers Caches Python
    print("ouvrir_nettoyage_cache")

    #---------nettoyage_cache AFFICHAGE---------
    print("AFFICHAGE")
    os.system('sudo python /home/pi/TravelKit_RPI/Affichage/DOT3K/nettoyage_du_cache.py')    
    #---------nettoyage_cache AFFICHAGE---------

    #---------nettoyage_cache GENERAL---------
    print("GENERAL")
    os.system('sudo python /home/pi/TravelKit_RPI/General/nettoyage_du_cache.py')    
    #---------nettoyage_cache GENERAL---------

    #---------nettoyage_cache GPS---------
    print("GPS")
    os.system('sudo python /home/pi/TravelKit_RPI/GPS/nettoyage_du_cache.py')    
    #---------nettoyage_cache GPS---------

def ouvrir_lumiere():
    print("\n")
    #Fichier gérant la lumière aperçu du DOT3K
    print("ouvrir_lumiere")

    #---------LIGHT---------
    os.system('sudo python /home/pi/TravelKit_RPI/Affichage/DOT3K/light_blue_cyan.py')    
    #---------LIGHT---------

def ouvrir_temps_time():
    print("\n")
    print("ouvrir_temps_time")

    #---------temps_time---------
    os.system('sudo python /home/pi/TravelKit_RPI/Affichage/DOT3K/dot3k_affichage_temps_système.py')    
    #---------temps_time---------

def ouvrir_boussole():
    print("\n")
    print("ouvrir_boussole")
    
    #---------BOUSSOLE---------
    os.system('sudo python /home/pi/TravelKit_RPI/Affichage/DOT3K/dot3k_affichage_boussole.py')
    #---------BOUSSOLE---------
    
def ouvrir_Recuperation_Determination():
    print("\n")
    print("ouvrir_Recuperation_Determination")

    #---------Recuperation_Determination---------
    os.system('sudo python /home/pi/TravelKit_RPI/Affichage/DOT3K/dot3k_affichage_determination.py')    
    #---------Recuperation_Determination---------

def ouvrir_Meteo():
    print("\n")
    print("ouvrir_Meteo")
    
    #---------Meteo---------
    os.system('sudo python /home/pi/TravelKit_RPI/Affichage/DOT3K/dot3k_affichage_meteo.py')    
    #---------Meteo---------

def ouvrir_Meteo_3h():
    print("\n")
    print("ouvrir_Meteo_3h")
    
    #---------Meteo_3h---------
    os.system('sudo python /home/pi/TravelKit_RPI/Affichage/DOT3K/dot3k_affichage_meteo_3h.py')    
    #---------Meteo_3h---------

def ouvrir_emergency_number():
    print("\n")
    print("ouvrir_emergency_number")
    
    #---------emergency_number---------
    os.system('sudo python /home/pi/TravelKit_RPI/Affichage/DOT3K/dot3k_affichage_emergency_number.py')    
    #---------emergency_number---------

def lancement():
    while True:
        print("\n")
        print("Ouverture de la Fonction 'lancement'")
        
        ouvrir_nettoyage_cache()
        time.sleep(2)
        ouvrir_lumiere()
        time.sleep(2)
        ouvrir_temps_time()
        time.sleep(3)
        
        ouvrir_emergency_number()
        time.sleep(5)
        ouvrir_boussole()
        time.sleep(13)
        ouvrir_Recuperation_Determination()
        time.sleep(13)
        ouvrir_Meteo()
        time.sleep(13)
        ouvrir_Meteo_3h()
        time.sleep(5)

if __name__ == "__main__":
    lancement()
    
