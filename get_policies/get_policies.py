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
from bs4 import BeautifulSoup

# Creating an useragent for certain servers that reject
# requests without user agents.
header = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
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

for pair in pairs:
  req = requests.get(pair[1], headers=header)
  content = BeautifulSoup(req.content, 'html.parser')

  print( content ) 


#  page = urllib.request.Request(pair[1])         # Making request to page.
#  page.add_header("User-Agent", "aUserAgent")
#  page = urllib.request.urlopen(pair[1]).read()
  #page = BeautifulSoup(page, 'html.parser')
  print("done")

#  pageContent = str(page)                         # Getting content as string.

  fp = open( pair[0]+".txt", 'x' )                # Writing content to a custom file
  fp.write(pageContent)
