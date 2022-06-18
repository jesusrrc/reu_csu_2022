#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario (Mercer University)
# Date:        06/15/2022
# Advisor:     Dr. Lydia Ray.
# Description: Python script to extract links for potential IoT companies' privacy policies 
#              from the names text file. In order to store the links to a text file, please
#              pipe the standard output in this fashion:
#
#                python3 get_policies_links.py > links.txt 
#
#########################################################################################

# Importing libraries.
import time
import requests
import urllib
from googlesearch import search

#########################################################################################
#
# Function #1
#
# Pre: Takes the name of a company.
# Pos: Outputs the company's name and a link to their privacy policy.
#
#########################################################################################

def searchPolicy( companyName ):
  query = companyName + " privacy policy"
  for x in search(query, tld="co.in", num=1, stop=1, pause=2):
    print(companyName+" "+x)

#########################################################################################
#
# Main function.
#
#########################################################################################

# Opening file with names and reading the names.
fp    = open("iot_names_3", "r")
names = fp.readlines()

# Stripping any newlines or extra spaces from the names.
for i in range(0,len(names)):
  names[i] = names[i].strip()

for x in range(0,len(names)):
  searchPolicy(names[x])          # For every 100 requests, we sleep for one minute, as
  if( x + 1 % 100 == 0 ):         # to not overload Google with too many requests.
    time.sleep(60.0)
