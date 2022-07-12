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
import os
import sys

#########################################################################################
#
# Main function:
#
#########################################################################################

# Opening valid CSV file.
myFiles = os.listdir("results_final") 

for myFile in myFiles:
  name = myFile
  myFile = open("results_final/"+myFile, "r")

  # Getting text lines from file.
  lst = myFile.readlines()

  # Extracting number of words in each file.
  val = lst[18].split(";")[1]
  val = int(val)
  print( val ) 

  if( val >= 100 ):
    os.system( "cp ../get_policies/clean_policies/"+name+" ./../final" )
