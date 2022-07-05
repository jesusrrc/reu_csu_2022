#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario
# Date:        06/22/2022
# Advisor:     Dr. Lydia Ray
# Description: Python script to obtain a readability assessment from the datasets, including
#              our own dataset.
#
#########################################################################################

# Used libraries.
import readability
import nltk
nltk.download('punkt')
import os
import sys
import re

#########################################################################################
#
# Function #1:
#
# Pre: Gets an array filled with the sentences from a text file.
# Pos: Returns the average number of words/tokens.
#
#########################################################################################

def avgNumWords( sentences ):
  avg = 0

  for x in sentences:                         # Collecting the total number of tokens.
    avg = avg + len(nltk.word_tokenize(x))

  avg = float( avg / len(sentences) )         # Calculating average.
  return avg 

#########################################################################################
#
# Function #2:
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

# Getting command line arguments (note that things will crash given wrong argument(s) ).
fileName = sys.argv[1]

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
for sent in sentences:
  text = text + " " + sent

"""
# Making report.
print("File name = ", fileName )
print("Number of sentences = ", len(sentences), "\nAverage number of words", avgNumWords(sentences) ) 
readabi = readability.Readability(text)
print( "ARI Score = ", readabi.ari() ) 
print( "FK = ", readabi.flesch_kincaid() )
print( "G-Fog = ", readabi.gunning_fog() )
"""

# Making report.
results = readability.getmeasures(text, lang='en')
print("File name = ", fileName )
print( results['readability grades'], '\n' )
print( results['sentence info'], '\n' )
print( results['word usage'],'\n' )
