#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario (Mercer University)
# Date:        06/16/2022
# Advisor:     Dr. Lydia Ray.
# Description: Python script used to extract text information from potential IoT privacy 
#              policies
#
#########################################################################################

# Used libraries.
import urllib.request
import time
import re
import os
from bs4 import BeautifulSoup

# Defining tags to help us define which content to preserve.
tags = [ 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'p', 'li' ] 

#########################################################################################
#
# Function #1:
#
# Pre: Takes the name of a valid file in raw_policies.
# Pos: Cleans a given policy and stored the resulting file in clean_policies.
#
#########################################################################################

def cleanPolicy( fileName ):

  # Opening a file pointer to write clean policy.
  writer = open('res2/'+str(fileName), 'x')

  # Getting content from the raw_policies folder.
  fp = open('raw_policies/'+str(fileName) )
  soup = BeautifulSoup(fp )

  # Instatiating a list to store the sentences/tokens.
  myList = list()

  # Algorithm adapted from "Applied Text Analysis with Python," by Bengfort 
  # et. al (pg. 41-42).
  for element in soup.find_all(tags):
    if( element.text != "" and element.text != "\n" ):
      x = element.text
      x = x.strip()
      x = x.replace('\n', '')
      myList.append(x)

  # Destroying the tree when finishing a given file, as to reduce memory use.
  soup.decompose()

  # Writing cleaned policy to a file in the clean_policies folder.
  for x in myList:
    writer.write(x+'\n')

  # Closing file pointers.
  writer.close()
  fp.close()

#########################################################################################
#
# Main function:
#
#########################################################################################

# Opening folder with raw policies to get their names.
fileNames = os.listdir("./raw_policies")
 
# Cleaning each policy.
for filename in fileNames:
  cleanPolicy( filename )

