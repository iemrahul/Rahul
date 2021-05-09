from copy import deepcopy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans


sns.set()

plt.rcParams['figure.figsize'] = (16,9)
plt.style.use('ggplot')
data = pd.read_csv('movie_metadata.csv')
kmeans = KMeans(n_clusters=10)

newdata = data.iloc[:,4:6]
newdata.dropna(inplace=True)
kmeans.fit(newdata)
kmeans.cluster_centers_
kmeans.labels_
unique,counts = np.unique(kmeans.labels_,return_counts=True)
newdata['cluster'] = kmeans.labels_
sns.set_style('whitegrid')
sns.lmplot('director_facebook_likes','actor_3_facebook_likes',data=newdata,hue='cluster',palette='coolwarm',height=6,aspect=1,fit_reg=False)
plt.show()