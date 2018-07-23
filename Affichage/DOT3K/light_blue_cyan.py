#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import dot3k.lcd as lcd
import dot3k.backlight as backlight

from nettoyage_du_cache import clear_cache

#Fichier permettant de mettre en font une couleur pour que l'écran soit lisible

#Lumière -- DEBUT --
print("Affichage BLEU CYAN")
backlight.rgb(0, 255, 245)    #Paramètre RGB Lumiere
#Lumière -- FIN --
