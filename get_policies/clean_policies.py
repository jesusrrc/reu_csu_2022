#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario (Mercer University)
# Date:        06/16/2022
# Advisor:     Dr. Lydia Ray.
# Description: Python script used to extract text information from potential privacy 
#              policies. Ideally, this program should receive the links from the command
#              line arguments in this fashion:
#
#########################################################################################

# Used libraries.
import urllib.request
import time
import re
from bs4 import BeautifulSoup

# Defining tags to help us define which content to preserve.
tags = [ 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'p', 'li' ] 

# Getting content from the command-line.
link = 'https://www.ptc.com/en/documents/policies/privacy'
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page, 'lxml')

# Instatiating a list to store the sentences/tokens.
myList = list()

# Algorithm adapted from "Applied Text Analysis with Python," by Bengfort 
# et. al (pg. 41-42).
for element in soup.find_all(tags):
  if( element.text != "" and element.text != "\n" ):
    x = element.text
    x = re.sub("\{.*?\}","{}", x)
    x = re.sub("[\{\[].*?[\}\]]", "", x)
    x = x.lower()
    x = x.strip()
    myList.append(x)

# Destroys the tree when finishing a given file, as to reduce memory use.
soup.decompose()

# Removing empty entries with a list comprehension.
myList[:] = [x for x in myList if x != "" ]


print( myList )

#html = "policy_thingworx.html"
#soup = bs4.BeautifulSoup(html, 'lxml')


