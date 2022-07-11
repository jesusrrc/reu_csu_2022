#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario (Mercer University)
# Date:        07/11/2022
# Advisor:     Dr. Lydia Ray.
# Description: 
#
#########################################################################################

# Used libraries.
import urllib.request
import time
import re
import os
import language_tool_python
from bs4 import BeautifulSoup

#########################################################################################
#
# Function #1:
#
# Pre: Gets a string denoting a sentence.
# Pos: Returns the sentence with a period.
#
#########################################################################################

def makeSentence( sentence ):
  ch = sentence[len(sentence)-1]

  if( ch == ';' or ch == ':' or ch == '!' ):   # Case 1: These punctuations should be
    sentence = sentence[0:len(sentence)-1]     # replaced by periods.
    sentence = sentence + '.'
    return sentence
  elif( ch == '.' ):                           # Case 2: A sentence already has its period.
    return sentence
  else:                                        # Case 3: Any other character implies that
    sentence = sentence + '.'                  # we need a period.
    return sentence

#########################################################################################
#
# Main function:
#
#########################################################################################

# Making list to store fully cleaned sentences and a very long string
# to retrieve the readability scores..
sentences = list()
text = ""

# Opening folder with raw policies to get their names.
fileNames = os.listdir("./res3")
 
# Cleaning each policy.
for i in range(0,len(fileNames)):
  fileNames[i] = "./res3/" + fileNames[i]

for fileName in fileNames:

  # Opening valid CSV file.
  myFile = open(fileName, newline='')

  # Getting text lines from file.
  lst = myFile.readlines()

  # Code to remove url's.
  # Source: https://java2blog.com/remove-urls-from-text-python/
  x = ""
  for line in lst:
    x = line.strip()
    x = re.sub('http://\S+|https://\S+', '', x)
    x = re.sub('\S*@\S*\s?', '', x)
    sents = x.split('.')

    for y in sents:                           # Getting sentences.
      if( y != '' ):
        y = makeSentence(y)
        sentences.append(y.strip()+'\n')      # The readability module needs newline
                                              # to recognize sentences.

tool = language_tool_python.LanguageTool('en-US')
for sent in sentences:
  print(tool.check(sent))
  print(sent)
