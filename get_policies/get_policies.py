#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario (Mercer University)
# Date:        06/16/2022
# Advisor:     Dr. Lydia Ray.
# Description: Python script used to get the raw HTML files of privacy policies into the
#              raw policies folder. We moved all the produced files into the raw_policies
#              folder.
#
#########################################################################################

# Used libraries.
import requests
import sys
import urllib.request
import time
import re
import itertools
from bs4 import BeautifulSoup

# Creating an useragent for certain servers that reject
# requests without user agents.
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

# Arrays to store companies and their links.
pairs = list()

# Opening file with links.
fp = open("links_7", "r")

for pair in fp: 
  pair = pair.split( "http" )   # Using the "http" token to split
  pair[1] = "http"+pair[1]      # and adding it back.

  pair[0] = pair[0].strip()     # Stripping any newlines
  pair[1] = pair[1].strip()     # and adding pairs to list.
  pairs.append( pair )

fp.close()                      # Closing first reader.

# Removing duplicates.
pairsS = set(tuple(x) for x in pairs)
pairs  = [ list(x) for x in pairsS ]

print( len(pairs) ) 

# A regular expression to remove special characters from names.
regex = re.compile('[^a-zA-Z0-9]')

for pair in pairs:
  flag = 1                                                       # Resetting flag and printing pair.
  print(pair)

  if( pair[1][len(pair[1])-3:len(pair[1])] == "pdf" ):           # A check to procure we are not using a PDF file.
    flag = 0

  try: 
    req = requests.get(pair[1], headers, timeout=10)             # Making request with header.
  except:
    print("Found an error while accessing site.")
    flag = 0

  if( flag == 1 ):
    pageContent = BeautifulSoup(req.content, 'html.parser')      # Opening html file and writing
    fp = open( regex.sub('',pair[0])+".txt", 'x' )          # content to a text file.
    fp.write(str(pageContent))
    fp.close()
