#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario
# Date:        07/12/2022
# Advisor:     Dr. Lydia Ray
# Description: 
#
#########################################################################################

# Used libraries.
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import statistics

#########################################################################################
#
# Main function:
#
#########################################################################################

# Opening valid CSV file.
myFiles = os.listdir("./results_final") 

m0 = [] # IDs.

# Arrays for readability scores.

m1 = []  # kincaid
m2 = []  # ari
m3 = []  # coleman_liau
m4 = []  # flesch
m5 = []  # gfi
m6 = []  # lix
m7 = []  # smog 
m8 = []  # rix
m9 = []  # dci

# Arrays of x per y.

m10 = [] # characters per word
m11 = [] # syllabes per word
m12 = [] # words per sentence

# Arrays of sentence elements.

m16 = [] # characters
m17 = [] # syllables
m18 = [] # words
m19 = [] # sentences
m24 = [] # tobeverbs
m25 = [] # auxiliary verbs.
m26 = [] # conjuctions
m27 = [] # pronouns
m28 = [] # prepositions

i = 0
for myFile in myFiles:
  name = myFile
  myFile = open("./results_final/"+myFile, "r")

  # Getting text lines from file.
  lst = myFile.readlines()

  # Getting number of words.
  val = lst[18].split(";")[1]
  val = int(val)
  
  if( val >= 100 ):

    # Making file indices.
    m0.append(i)
    i = i + 1

    # Appending scores.
    m1.append( float(lst[1].split(";")[1]) )
    m2.append( float(lst[2].split(";")[1]) )
    m3.append( float(lst[3].split(";")[1]) ) 
    m4.append( float(lst[4].split(";")[1]) )        
    m5.append( float(lst[5].split(";")[1]) ) 
    m6.append( float(lst[6].split(";")[1]) ) 
    m7.append( float(lst[7].split(";")[1]) ) 
    m8.append( float(lst[8].split(";")[1]) ) 
    m9.append( float(lst[9].split(";")[1]) ) 

    # Appending other properties.
    m10.append( float(lst[10].split(";")[1]) ) 
    m11.append( float(lst[11].split(";")[1]) ) 
    m12.append( float(lst[12].split(";")[1]) ) 

    # Appending primary properties.
    m16.append( float(lst[16].split(";")[1]) ) 
    m17.append( float(lst[17].split(";")[1]) ) 
    m18.append( float(lst[18].split(";")[1]) ) 
    m19.append( float(lst[19].split(";")[1]) ) 
    m24.append( float(lst[24].split(";")[1]) ) 
    m25.append( float(lst[25].split(";")[1]) ) 
    m26.append( float(lst[26].split(";")[1]) ) 
    m27.append( float(lst[27].split(";")[1]) ) 
    m28.append( float(lst[28].split(";")[1]) ) 

print( len(m0), len(m1) ) 

y_axes = [ "kincaid", "ari", "coleman_liau", "flesch", "gfi", "lix", "smog", "rix", "dci", "chars_per_words", "syll_per_words",
"words_per_sent", "chars", "syll", "words", "sents", "to_be_verbs", "aux_verbs", "conjunctions", "pronouns", "prepositions"
]

data = [ m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m16, m17, m18, m19, m24, m25, m26, m27, m28 ]

titles = [
  "Kincaid Grade Level",
  "Automated Readability Index (ARI)",
  "Coleman-Liau Index",
  "Flesch Reading Ease Test",
  "Gunning Fog Index",
  "Lix Readability Formula",
  "SMOG Readability Formula",
  "Rix Readability Test",
  "Dale-Chall Index",
  "Characters per Word",
  "Syllables per Word",
  "Words per Sentence",
  "Number of Characters",
  "Number of Syllables",
  "Number of Words",
  "Number of Sentences",
  "Number of Be Verbs",
  "Number of Auxilliary Verbs",
  "Number of Conjunctions",
  "Number of Pronouns",
  "Number of Prepositions"
]

# Statistical report.
for i in range( 0, len(y_axes) ):
  print(titles[i])
  print( max(data[i]), statistics.median(data[i]), sum(data[i])/float(len(data[i])) )

# Data plots.
for i in range( 0,len(y_axes) ):
  plt.title( titles[i] ) 
  plt.scatter( m0, data[i], s=[2 for n in range(len(m0))] )
  plt.xlabel( "file_ids" )
  plt.ylabel( y_axes[i] )
  plt.savefig( str(i)+'.pdf' )
  plt.clf()
