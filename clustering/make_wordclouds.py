#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario
# Date:        07/18/2022
# Advisor:     Dr. Lydia Ray
# Description: Python script to showcase the results of k-clustering with word clouds.
#              This program assumes that we generated 12 separate topics.
#
#########################################################################################

# Imports for data visualization.
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#########################################################################################
#
# Main function:
#
#########################################################################################

# Opening sample results.
fp = open("sample_results.txt", "r" )
tmp = list()

# Building array of array of words.
for w in fp:
  tmp.append(w)

# Generating wordclouds.
for i in range(12):
  wc = WordCloud(width=1000, height=600, margin=3, prefer_horizontal=0.7,scale=1,
  background_color='white', relative_scaling=0).generate(tmp[i])
  plt.imshow(wc)
  plt.title(f"Topic{i+1}")
  plt.axis("off")
  plt.savefig(str(i+1)+'.pdf')
