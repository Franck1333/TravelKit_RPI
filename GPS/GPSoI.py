#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides: https://stackoverflow.com/questions/24906833/get-your-location-through-python
#Aides: https://github.com/Franck1333/GPS-Display/blob/master/Mon_Travail/Recuperation_Determination.py

import requests     #<-- Utilisation d'une Adresse URL Normalisée
import json         #<-- Permet l'expoitation de fichier en format JSON
import googlemaps   #pip install -U googlemaps <-- API Python de Google MAPS

import unicodedata #Cette blibliothèque permet de travailler avec du contenue contenant des accents

from nettoyage_du_cache import clear_cache

#EXPLICATION --DEBUT--
#Ce Programme est utile pour determine la localisation de l'Adresse IP de l'utilisateur
#En revanche , ce programme n'indique pas la localisation exacte de l'utilisateur, dans ce cas elle sera imprécise!!!
#EXPLICATION --FIN--


#----------
#API https://ipstack.com

def recuperation_coordonees_ip():

    send_url = 'http://api.ipstack.com/check?access_key=b0e724b68c170a901019d01552425f1a&format=1'
    r = requests.get(send_url)      #<-- Ouverture de L'URL pour l'utilisation de L'API
    j = json.loads(r.text)          #Chargement des données reçu dans le fichier en format JSON

    global latitude                 #Declaration de la variable Globale 'latitude'
    global longitude                #Declaration de la variable Globale 'longitude'

    #Information Technique --DEBUT--
    ip = j['ip']
    print("Voici votre adresse I.P:", ip)
    #Information Technique --FIN--

    #Information Géographique --DEBUT--
    latitude = j['latitude']        #Enregistrement de la valeur latitude du fichier JSON dans la Variable Global correspondant
    longitude = j['longitude']      #Enregistrement de la valeur longitude du fichier JSON dans la Variable Global correspondant

    city = j['city']
    region_name = j['region_name']
    ZIP = j['zip']
    country_name = j['country_name']

    global continent_name
    continent_name = j['continent_name']
    
    print(latitude)                 #Affichage de la Variable 'latitude'
    print(longitude)                #Affichage de la Variable 'longitude'
    print(continent_name)
    print("L'adresse IP a ete localiser ici:",city)
    print("Les Coordonees exactes de l'Adresse IP utilise:",continent_name,country_name,region_name,ZIP,city)
    #Information Géographique --FIN--

    return continent_name,latitude,longitude     #Retourne le nom du continent où est localiser l'adresse I.P
    #return latitude,longitude                         #Retourne les variables obtenue dans le cadre d'une utilisation ultérieur de ses valeurs
#----------

#INFORMATION :
#La localisation de exacte de l'adresse IP peut être obtenue via l'API /api.ipstack.com/ ou alors en donnant les deux valeurs latitude et longitude à une autre
#A.P.I tel que Google MAPS, qui lui peut obtenir des résultats différents ou plus précis que la première API ; A vous de choisir.

#----------
#API https://console.cloud.google.com/

def determination():

    gmaps = googlemaps.Client(key='AIzaSyCbcLmcGDUQlhvZhAkdE0IUFh90rjJ7rrw')            #Cle d'acces A.P.I

    reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))               #Envoie et Recuperation des Donnees
    
    print("L'Adresse IP Localise a :")
    #print(reverse_geocode_result) Format JSON

    resultat_Adresse = reverse_geocode_result[0]['formatted_address']                   #STRING LOCALISATION DETERMINE de L'Adresse entière    
    resultat_Ville = reverse_geocode_result[0]['address_components'][2]['long_name']    #STRING LOCALISATION DETERMINE de La Ville uniquement

    print ("A l'Adresse suivante :",resultat_Adresse)                                   #Affichage de l'adresse entière determinée 
    print ("Dans la ville de :",resultat_Ville)                                         #Afficgage de la Ville determinée

    return resultat_Adresse,resultat_Ville #Retourne les variables obtenue dans le cadre d'une utilisation ultérieur de ses valeurs
#----------

if __name__ == "__main__":
    clear_cache()
    recuperation_coordonees_ip()    #Fonctionnalité permettant d'Obtenir/Determiné les coordonées GPS correspondant à l'Adresse I.P de l'utilisateur
    #determination()                 #Fonctionnalité permettant de determiné la localisation de l'utilisateur avec son adresse I.P avec Google MAPS
    
