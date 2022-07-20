#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario
# Date:        06/28/2022
# Advisor:     Dr. Lydia Ray
# Description: Python script to perform k-clustering on the dataset. The main premise of 
#              k-clustering is to use unsupervised learning to infer categories from our
#              datasets.
#
#########################################################################################

# Used libraries.
import os
import pandas as pd
import wikipedia
import matplotlib.pyplot as plt
import numpy

# Imports from NLTK (stopwords).
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Imports for SKLearn (machine learning).
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

#########################################################################################
#
# Main function:
#
#########################################################################################

# Getting the filenames for all the cleaned privacy policies.
fileNames = os.listdir("./../final")

# Initializing arrays to store file contents and their titles.
fileContents = []
titles = []

# Extracting content into arrays.
for fileName in fileNames:
  fp = open("./../final/" + fileName, 'r')
  fileContents.append(str(fp.read()))
  titles.append(str(fileName))

# Vectorization.
vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
input_matrix = vectorizer.fit_transform(fileContents) 
svd_modeling= TruncatedSVD(n_components=12, algorithm='randomized', n_iter=5 )
svd_modeling.fit(input_matrix)
components=svd_modeling.components_
vocab = vectorizer.get_feature_names_out()

# Writing top-10 words per category/topic.
topic_word_list = []
def get_topics(components): 
  for i, comp in enumerate(components):
    terms_comp = zip(vocab,comp)
    sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:10]
    topic=" "
    for t in sorted_terms:
      topic= topic + ' ' + t[0]
    topic_word_list.append(topic)
  return topic_word_list

res = get_topics(components)
for x in res:
  print(x)
