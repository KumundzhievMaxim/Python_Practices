# -*- coding: utf-8 -*-
"""Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OBs8g2WLSUFQ_gimL0ZS514A0zF2c0Y3
"""

# Agglomerative clustering. ForestFires.
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

filename ='https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv'
df = pd.read_csv(filename)

data = df[['month','FFMC','DMC', 'DC']]

varieties = list(data.pop('month'))
samples = data.values
mergings = linkage(samples, method='complete')


dendrogram(mergings,
          no_labels=True,
          labels=varieties,
          leaf_rotation=90,
          leaf_font_size=10,
          )


plt.show()

# K-means method
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets
 
filename ='https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv'
df = pd.read_csv(filename)

f1 = df[['FFMC','DMC', 'DC']]
        
model = KMeans(n_clusters=3)
 
model.fit(f1)
predicted_label = model.predict([[7.2, 3.5, 0.8]])
all_predictions = model.predict(f1)
 
# print(predicted_label)
# print(all_predictions)

x = df['FFMC']
y = df['DMC']
plt.scatter(x,y)
plt.xlabel("FFMC")
plt.ylabel("DMC")
plt.show()

# DBSCAN//need to complete!!!
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename ='https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv'
df = pd.read_csv(filename)

df = df[["FFMC", "DMC"]]
df = df.as_matrix().astype("float32", copy = False)
stscaler = StandardScaler().fit(df)
df = stscaler.transform(df)
dbsc = DBSCAN(eps = .5, min_samples = 15).fit(df)
labels = dbsc.labels_
core_samples = np.zeros_like(labels, dtype = bool)
core_samples[dbsc.core_sample_indices_] = True
# df = df.astype(int)

# x = df['FFMC']
# y = df['DMC']
# plt.scatter(x,y)
# plt.xlabel("FFMC")
# plt.ylabel("DMC")
# plt.show()

