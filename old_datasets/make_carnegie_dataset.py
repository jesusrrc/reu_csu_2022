#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario (Mercer University)
# Date:        06/13/2022
# Advisor:     Dr. Lydia Ray.
# Description: Python script to write the Carnegie Mellon plaintext dataset into
#              a CSV file. The program uses command-line arguments to handle the
#              files (no error-handling included).
#
#########################################################################################

# Libraries.
import sys
import csv
import ast
import re

data = []

# Taking input and output files.
fileIn  = str(sys.argv[1])
fileOut = str(sys.argv[2])






#loop until all requested files are processed
#while filename != "exit":
#    entry = list(csv.reader(open(filename)))
    
    #make data
#    for line in annotations:
        #category label
#        category = line[5]
        #skip all labled "Other"  
#        if category != "Other":
#            if category == "Policy Change":
#                print("change")
#            text = []
#            #get dictionary
#            text_dict = ast.literal_eval(line[6])
#            outer_keys = text_dict.keys()
#            #find all instances of text selections
#            for key in outer_keys:
#                inner_keys = text_dict[key].keys()
#                if 'selectedText' in inner_keys:
#                    new_text = text_dict[key]['selectedText'].lower()
#                    if new_text != 'null' and new_text != 'not selected':
#                        text.append(new_text)
#            #clean text
#            text = ' '.join(text)
#            text = re.sub(r'[^\w\s]','',text)
#            data.append([text,category])
  
#    #get next file
#    filename = input("File path: ")

#filename = input("Name of save file: ")
#save_file = csv.writer(open(filename,'w'))
#save_file.writerows(data)
