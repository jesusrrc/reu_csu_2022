#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario
# Date:        06/28/2022
# Advisor:     Dr. Lydia Ray
# Description: Python script to perform k-clustering on the dataset.
#
#########################################################################################

# Used libraries.
import os
import pandas as pd
import wikipedia
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Getting the filenames for all the cleaned privacy policies.
fileNames = os.listdir("../get_policies/clean_policies")

# Initializing arrays to store file contents and their titles.
fileContents = []
titles = []

# Extracting content into arrays.
for fileName in fileNames:
  fp = open("../get_policies/clean_policies/" + fileName, 'r')
  fileContents.append(str(fp.read()))
  titles.append(str(fileName))

# Vectorization.
vectorizer = TfidfVectorizer(stop_words={'english'})
X = vectorizer.fit_transform(fileContents) 

"""
# K-Means clustering.
Sum_of_squared_distances = []
K = range(2,500)
for k in K:
   km = KMeans(n_clusters=k, max_iter=200, n_init=10)
   km = km.fit(X)
   Sum_of_squared_distances.append(km.inertia_)

# Making plot.
plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.savefig('foo.pdf')
"""

# Vectorization.
true_k = 6
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=200, n_init=10)
model.fit(X)
labels=model.labels_
wiki_cl=pd.DataFrame(list(zip(titles,labels)),columns=['title','cluster'])
#print(wiki_cl.sort_values(by=['cluster']))

# Printing/displaying dataframe.
print(wiki_cl.to_string())
