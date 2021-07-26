# -*- coding: utf-8 -*-
"""Practical 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wUR96xiXkOxEyFkOBG82x69XUrYrq8Aq

# Load the data from wine dataset. Check whether all attributes are standardized or not (mean is 0 and standard deviation is 1). If not, standardize the attributes. Do the same with Iris dataset.

# Wine Dataset
"""

import pandas as pd
import matplotlib.pyplot as plt
wine=pd.read_csv('https://gist.githubusercontent.com/tijptjik/9408623/raw/b237fa5848349a14a14e5d4107dc7897c21951f5/wine.csv')
wine

"""## Checking standardization"""

pd.set_option("display.max_rows", None, "display.max_columns", None)
wine.groupby('Wine').describe().transpose()

"""## Visualization

Before Standardisation
"""

wine['Alcohol'].hist(figsize=(10,10))
wine.hist(figsize=(10,10),legend=True)
for i in range(1,wine.shape[1]):
  column=wine.columns[i]
  print("Mean",column,round(wine[column].mean(),4))

"""Scaling/Standardising Data"""

pd.set_option("display.max_rows", 10, "display.max_columns", None)
from sklearn.preprocessing import scale 

l = []
for i in wine.columns:
  if wine[i].mean() != 0 and wine[i].std() != 1 and i != 'Wine':
    l.append(True)
  else:
    l.append(False)

std_wine = wine[wine.columns[l]]
std_wine

pd.set_option("display.max_rows", 10, "display.max_columns", None)
std_wine = scale(std_wine)
wine[wine.columns[l]] = pd.DataFrame(std_wine,columns=wine.columns[l])
wine

pd.set_option("display.max_rows", None, "display.max_columns", None)
wine.groupby('Wine').describe().transpose()

wine['Alcohol'].hist(figsize=(10,10))
wine.hist(figsize=(10,10),legend=True)

M=[]
SD=[]
for i in wine:
  if i != 'Wine':
    M.append(round(wine[i].mean()))
    SD.append(round(wine[i].std()))
Scaled=pd.DataFrame(data=(M,SD),columns=wine.columns[1:],index=('Mean','Standard Deviation'))
Scaled.transpose()

"""# Iris dataset"""

pd.set_option("display.max_rows", 10, "display.max_columns", None)
iris = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv')
iris

iris.hist(figsize=(10,10))
iris[:].hist(by=iris['species'],figsize=(10,10),legend=True)
plt.show()

iris.groupby('species').describe().transpose()

l = []
for i in iris.columns:
  if i != 'species' and iris[i].mean() != 0 and iris[i].std() != 1 :
    l.append(True)
  else:
    l.append(False)

scd = iris[iris.columns[l]]

scaled = scale(scd)
iris[iris.columns[l]] = pd.DataFrame(scaled,columns=iris.columns[l])
pd.set_option("display.max_rows", 10, "display.max_columns", None)
iris

"""Standardising Dataset"""

M=[]
SD=[]
for i in iris:
  if i != 'species':
    M.append(round(iris[i].mean()))
    SD.append(round(iris[i].std()))
Scaled=pd.DataFrame(data=(M,SD),columns=iris.columns[:-1],index=('Mean','Standard Deviation'))
Scaled.transpose()

ax1=iris[:].hist(figsize=(10,10))
ax2=iris[:].hist(by=iris['species'],figsize=(10,10),legend=True)

!cp  '/content/drive/MyDrive/Colab Notebooks/Practical 3.ipynb' ./
!jupyter nbconvert --to html "Practical 3"