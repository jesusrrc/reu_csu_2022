#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario (Mercer University)
# Date:        06/16/2022
# Advisor:     Dr. Lydia Ray.
# Description: Python script used to get the raw HTML files of privacy policies into the
#              raw policies folder.
#
#########################################################################################

# Used libraries.
import urllib.request
import time
import re
from bs4 import BeautifulSoup

# Arrays to store companies and their links.
companies = list()
links =     list()

# Opening file with links.
fp = open("links_7", "r")

for pair in fp: 
  pair = pair.split( "http" )   # Using the "http" token to split
  pair[1] = "http"+pair[1]      # and adding it back.

  pair[0] = pair[0].strip()     # Stripping any newlines.
  pair[1] = pair[1].strip()
  
  companies.append(pair[0])     # Adding each name and link to 
  links.append(pair[1])         # the right arrays.

for link in links:
  page = urllib.request.urlopen(link)           # Making request to page.
  page = BeautifulSoup(page, 'lxml')

  pageContent = str(page)                       # Getting content as string.

  fp = open( link+".txt", "x" )                 # Writing content to a custom file
  fp.write( pageContent )                       # and sleeping for a second.
  time.sleep(1.0)
