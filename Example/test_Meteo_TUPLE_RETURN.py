#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial
import time
import os
import sys

from Meteo import main_meteo

#from Meteo import Vitesse_du_vent
#from Meteo import Status_climat
#from Meteo import Volume_de_neige
#from Meteo import Volume_de_pluie
#from Meteo import Couverture_de_nuage
#from Meteo import Pourcentage_humidite
#from Meteo import Lever_du_soleil
#from Meteo import Coucher_du_soleil

def main_test():
    print("OBJECTIF: Obtenir plusieurs valeurs meteo.")
    print("Pour obtenir plusieurs valeurs provenant d'un return , on doit utiliser les TUPLES")
    #print(main_meteo())

    test_climat_min,test_climat_max,test_climat_now,test_vitesse_du_vent,test_status_climat,test_volume_de_neige,test_volume_de_pluie,test_couverture_de_nuage,test_pourcentage_humidite,test_lever_du_soleil,test_coucher_du_soleil = main_meteo()

    print("test_climat_min", test_climat_min)
    print("test_climat_max", test_climat_max)
    print("test_climat_now", test_climat_now)
    print("test_vitesse_du_vent", test_vitesse_du_vent)
    print("test_status_climat", test_status_climat)
    print("test_volume_de_neige", test_volume_de_neige)
    print("test_volume_de_pluie", test_volume_de_pluie)
    print("test_couverture_de_nuage", test_couverture_de_nuage)
    print("test_pourcentage_humidite", test_pourcentage_humidite)
    print("test_lever_du_soleil", test_lever_du_soleil)
    print("test_coucher_du_soleil", test_coucher_du_soleil)



if __name__ == "__main__":
    main_test()
