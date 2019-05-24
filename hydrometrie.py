# TODO: tout
# TODO: cf regularite ter pour avoir une idée de quoi faire

# IDEA: qqn à compris le sqlite ?

import http.server
import socketserver
from urllib.parse import urlparse, parse_qs, unquote
import json

import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as pltd

import sqlite3

#
# Définition du nouveau handler
#
class RequestHandler(http.server.SimpleHTTPRequestHandler):

  # sous-répertoire racine des documents statiques
  static_dir = '/client'


# =============== Main program ===============
if __name__ == "__main__":
