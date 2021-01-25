

## Getting Started with Pandas

import pandas as pd

x = pd.Series([6,3,8,6])
x = pd.Series([6,3,8,6], index=["q", "w", "e", "r"])

data = { 'name' : ['Tim', 'Jim', 'Pam', 'Sam'],
         'age' : [29,31,27,35],
         'zip' : ['02115', '02130', '67700', '00100']}

x = pd.DataFrame(data, columns=["name", "age", "zip"])

x["name"]
x.name
sorted(x.index)
x.reindex(sorted(x.index))

y = pd.Series([7,3,5,2], index=["e", "q", "r", "t"])


## Loading and Inspecting Data 

import numpy as np
import pandas as pd

cd /home/andrea32/Python4Research/Week4

whisky = pd.read_csv("whiskies.txt")

whisky["Region"] = pd.read_csv("regions.txt")

whisky.head()
whisky.tail()

whisky.iloc[5:10, 0:5]
whisky.columns

flavors = whisky.iloc[:, 2:14]


## Exploring Correlations

flavors 

corr_flavors = pd.DataFrame.corr(flavors)
print(corr_flavors)

import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")


corr_whisky = pd.DataFrame.corr(flavors.transpose())
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whisky.pdf")

## Clustering Whiskies By Flavor Profile

from sklearn.cluster.bicluster import SpectralCoclustering 
model = SpectralCoclustering(n_clusters=6, random_state=0)

model.fit(corr_whisky)
model.rows_

np.sum(model.rows_, axis=1)

np.sum(model.rows_, axis=0)

model.row_labels_

## Comparing Correlation Matrices

whisky['Group'] = pd.Series(model.row_labels_, index=whisky.index)
whisky = whisky.iloc[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)

correlations = pd.DataFrame.corr(whisky.iloc[:, 2:14].transpose())
correlations = np.array(correlations)

plt.figure(figsize = (14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.savefig("correlations.pdf")

### Homework

import pandas as pd
data = pd.Series([1,2,3,4])
data = data.iloc[[3,0,1,2]]









