# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:31:34 2021

@author: Maddox
"""

import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display

os.getcwd()

data = pd.read_csv('500 richest people 2021.csv', sep=';')

data.head()
data.tail()

data = data[:499]
data.tail()

list(data.columns)

data = data.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], axis = 1)
data = data.rename(columns = {'Total Net Worth':'Worth'})

data['Worth'] = data['Worth'].str.replace('B', '')
data

#Name = data.Name
#Worth = data.Worth

#Horizantal Bar PLOT
country_counts = data['Country'].value_counts(ascending=True)
country = pd.Series(list(country_counts.index))
country_counts.index = range(len(country_counts))

fig, ax = plt.subplots(figsize=(12,12))
ax.barh(country, country_counts)
ax.set_title('Distribution of the Wealthiest by Country')
ax.set_xlabel('Number of the Weathiest')
ax.set_ylabel('Countries')
ax.set_yticklabels(country, fontsize=7)
plt.show()

#Vertical Bar Plot
industry_counts = data['Industry'].value_counts(ascending=True)
industry = pd.Series(list(industry_counts.index))
industry_counts.index = range(len(industry_counts))

fig, ax = plt.subplots()
ax.bar(industry, industry_counts)
ax.set_title('Distribution of the Wealthiest by Industry')
ax.set_xlabel('Industry')
ax.set_xticklabels(industry, rotation = 90)
ax.set_ylabel('Number of Wealthiest')
ax.set_yticklabels(industry_counts, fontsize=10)
plt.show()


top50 = data[:50]
top50.tail()

#Scatterplot
worth = top50['Worth']
names = top50['Name']
industry_counts = top50['Industry'].value_counts(ascending=True)
industry = pd.Series(list(industry_counts.index))
industry_counts.index = range(len(industry_counts))

fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(names, worth)
ax.set_title('Total Worth of Top 500 Wealthiest People')
ax.invert_yaxis()
ax.set_xlabel('Indusrty')
ax.set_xticklabels(names, rotation = 90)
ax.set_ylabel('Total Net Worth')
ax.set_yticklabels(worth, fontsize=10)

plt.show()