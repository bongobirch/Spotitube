# Spotitube v1
# Jacob Birch & Wyatt Sillavan

import requests
import spotipy
import sys

modulename = 'spotipy'
if modulename not in sys.modules:
    print('You have not imported the {} module'.format(modulename))
else:
    print('is')
