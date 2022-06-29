"""
Title: PurExt Implementation
Author: Vincent Miller
Date: 13 June 2022
Description: Implement the PurExt algorithm to pull purpose-aware rules from privacy policies
    See notes.txt for more details
"""
import spacy
import classifier
from spacy import displacy

# PurExt examples
s1 = "The purpose of collecting your location data and speed is to analyze your train statistics."  # explicit
# r1({},{“collect”},{“your location data”,”speed”},{“analyze your train statistics”})
s2 = "The reason of using your name and e-mail address includes website account registration."  # explicit
# r2({}, {“use”}, {“Your name”, “e-mail address”}, {“website account registration”})
s3 = "The app will collect your heart rate and pulse to make suggestions for future workouts."  # implicit

# Because these sentences don't have periods (.), spacy doesn't tokenize them correctly.
# my attempt to add . to the end of every line
with open("Plain Text Policies/PurExtSents.txt", 'r') as istr:
    with open('output.txt', 'w') as ostr:
        for line in istr:
            line = line.rstrip('\n') + '.'
            print(line, file=ostr)

nlp = spacy.load("en_core_web_sm")

file = open("output.txt", "r")
doc = nlp(file.read())
file.close()

# doc = nlp(s1 + " " + s2 + " " + s3)

classifier.sentence_classifier(doc)


# http://127.0.0.1:5000 to view dependency tree
# displacy.serve(doc, options={"compact": True, "collapse_phrases": True})`
