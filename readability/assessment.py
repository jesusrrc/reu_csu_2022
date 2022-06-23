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
import csv
import os
import sys

#########################################################################################
#
# Function #1:
#
# Pre: Gets an array filled with the sentences from a CSV dataset.
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
# Main function:
#
#########################################################################################

# Array and text to store sentences.
sentences = list()
text = ""

# Getting command line arguments (note that things will crash given wrong argument(s) ).
fileName = sys.argv[1]
column   = int(sys.argv[2])


# Opening valid CSV file.
myFile = open(fileName, newline='')
reader = csv.reader(myFile, delimiter=',')

# Storing sentences.
for row in reader:
  sentences.append(row[column])

print("File name = ", fileName, "\nColumn index = ", column )
print("Number of sentences = ", len(sentences), "\nAverage number of words", avgNumWords(sentences) ) 

# Building text for readability text.
for x in sentences:
  text = text + ".\n" + x

readabi = readability.Readability(text)
print( "ARI Score = ", readabi.ari() ) 
print( "FK = ", readabi.flesch_kincaid() )
print( "G-Fog = ", readabi.gunning_fog() )
