# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:11:47 2021

@author: Dell
"""
import pandas as pd

dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset.describe()
x=dataset['Title'].value_counts()
import matplotlib.pyplot as plt
plt.pie(x)
plt.show()

import pandas as pd
data =pd.read_csv("Wuzzuf_Jobs.csv")
data.sort_values("Title", inplace = True )
data.drop_duplicates(subset ="Title",
					keep = "first", inplace = True)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset.sort_values(by=["Title", "Company","Location","Type","Level","YearsExp","Country","Skills"], inplace=True)
x = dataset.iloc[:,[0]].values
y = dataset.iloc[:, 1].values
z = dataset.iloc[:, 2].values
c = dataset.iloc[:, 3].values
v = dataset.iloc[:, 4].values
b = dataset.iloc[:, 5].values
n = dataset.iloc[:, 6].values
m = dataset.iloc[:, 7].values


import pandas as pd

dataset=pd.read_csv("Wuzzuf_Jobs.csv")
q=dataset['Company'].value_counts()
import matplotlib.pyplot as plt
plt.pie(q)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
t=dataset['Title']
d=dataset['Title'].value_counts()
courses = list(t)
values = list(d)
plt.bar(courses, values, color ='red',
		width = 0.2)

plt.xlabel("Title")
plt.ylabel("Title.count")
plt.title(" Max.Title  ")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
p=dataset['Country']
o=dataset['Country'].value_counts()
courses = list(p)
values = list(o)
plt.bar(courses, values, color ='red',
		width = 0.2)

plt.xlabel("Country")
plt.ylabel("Country.count")
plt.title(" Max.Country  ")
plt.show()

import pandas as pd
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
p=dataset['Skills']
o=dataset['Skills'].value_counts()

