#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario (Mercer University)
# Date:        06/15/2022
# Advisor:     Dr. Lydia Ray.
# Description: Python script to extract IoT companies' names from
#              the iotone.com website. Ideally, the names should go into a file in this
#              fashion:
#
#                 python3 get_policy_names_iotone.py > iot_names_n 
#
#########################################################################################

# Importing libraries.
import urllib.request
import time
from bs4 import BeautifulSoup

for i in range(102):
  # Getting HTML document, using the index i to explore each page.
  link = 'http://iotone.com/suppliers?page='+str(i)
  page = urllib.request.urlopen(link)
  pageFinal = BeautifulSoup(page, 'html.parser')

  # Converting HTML content into string and splitting based
  # on newlines.
  pageContent = str(pageFinal) 
  pageContent = pageContent.split('\n')

  # Searching for the company names and removing surrounding
  # clutter. Particularly, we want to remove all the information
  # of the </a> tag EXCEPT for the company's name.
  for x in pageContent:    
      if "product-name" in x:
        x = x[x.find(">")+1:]
        x = x.replace("</a>", "")
        print(x)

  # Sleeping for a few seconds as to not encourage iotone.com to
  # block our machine's IP.
  time.sleep(5.0)
