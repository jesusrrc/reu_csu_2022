#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario (Mercer University)
# Date:        06/15/2022
# Advisor:     Dr. Lydia Ray.
# Description: Python script to extract top 100 industrial IoT companies' names from
#              an iotone.com article. Ideally, the names should go into a file in this
#              fashion:
#
#                 python3 get_policy_names.py > iot_names_n 
#
#########################################################################################

# Importing libraries.
import urllib.request
from bs4 import BeautifulSoup

# Getting HTML document.
link = 'http://iotone.com/iotone500'
page = urllib.request.urlopen(link)
pageFinal = BeautifulSoup(page, 'html.parser')

# Converting HTML content into string and splitting based
# on newlines.
pageContent = str(pageFinal) 
pageContent = pageContent.split('\n')

# Searching for the company names and removing surrounding
# clutter.
for x in pageContent:    
    if "record-name=" in x:
        x = x[x.find("record-name"):]
        x = x[:x.find("target")]
        x = x.replace("record-name=", "")
        x = x.replace("\"", "")
        print(x)
