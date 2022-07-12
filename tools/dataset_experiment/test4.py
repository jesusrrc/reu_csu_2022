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
 
# Instatiating grammar detectiob object.
tool = language_tool_python.LanguageTool('en-US')

for fileName in fileNames:

  # Resetting list of sentences.
  sents = []
  sentences = []

  # Opening valid CSV file.
  myFile = open("./res3/"+fileName, newline='')

  # Getting text lines from file.
  lst = myFile.readlines()

  # Code to remove url's.
  # Source: https://java2blog.com/remove-urls-from-text-python/
  x = ""
  for line in lst:
    x    = line.strip()                               # Removing clutter and making sentences with
    x    = re.sub('http://\S+|https://\S+', '', x)    # the help of regular expressions.
    x    = re.sub('www\S+', '', x)
    x    = re.sub('\S*@\S*\s?', '', x)
    temp = re.split(';|:|!|\.',x)

    for t in temp:                            # Appending sentences to bigger list.
      sents.append(t)

    for y in sents:                           # Building sentences.
      if( y != '' ):
        y = makeSentence(y)
        sentences.append(y.strip()+'\n')      

  # Writing results.
  writer = open("./res4/"+fileName, 'x')
  for sent in sentences:
    if( len(tool.check(sent)) == 0 ):
      writer.write(sent)
