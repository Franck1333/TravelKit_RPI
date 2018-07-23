#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides: https://gist.github.com/j4mie/557354 
 
import unicodedata

""" Normalise (normalize) unicode data in Python to remove umlauts, accents etc. """

data = u'naïve café'
normal = unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')
print normal
 
# prints "naive cafe"
