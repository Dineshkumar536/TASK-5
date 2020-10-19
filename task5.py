#DINESH KUMAR
#TASK - 5 PERFORMING EXPLORATORY ANALYSIS ON PROVIDED 'SAMPLE STORE DATASET'.


#IMPORTING LIBRARIES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#IMPORTING DATASET
dataset = pd.read_csv('SampleSuperstore.csv')
dataset.head()
dataset.shape

#CHECKING FOR MISSING DATA
dataset.isnull().sum()

#CHECKING FOR DUPLICATES AND DROP THEM
dataset.duplicated().sum()
dataset.drop_duplicates()
dataset.shape
dataset.nunique()

#EXPLORING DATASET INFO AND DESCRIBING IT
dataset.info()
dataset.describe()

#REMOVING IRRELEVANT VARIABLES (POSTAL CODE AND COUNTRY)
super_store = dataset.drop(['Postal Code'], axis=1)
super_store = dataset.drop(['Country'], axis=1)
super_store

#DESCRIPTIVE STATISTICS
super_store.describe()

#ANALYSING  AND VISUALISING CORRELATION AMONG VARIABLES
corrl = super_store.corr()
corrl
plt.figure(figsize=(12,6))
sns.heatmap(corrl, annot = True)
plt.show()

#EXPLORING THE DISTRIBUTION OF THE 'SUB-CATEGORY' PERTAINING TO 'CATEGORY' AND VISUALISING
super_store['Sub-Category'].value_counts()
plt.figure(figsize=(16,8))
plt.bar('Sub-Category', 'Category', data=super_store)
plt.show()

#MORE VISUALS OF INDIVIDUAL LABELS
print (super_store['Ship Mode'].value_counts())
plt.figure(figsize=(10,6))
sns.countplot(x=super_store['Ship Mode'])
plt.show()

print (super_store['Segment'].value_counts())
plt.figure(figsize=(10,6))
sns.countplot(x=super_store['Segment'])
plt.show()


print (super_store['City'].value_counts())
plt.figure(figsize=(15,6))
sns.countplot(x=super_store['City'], order=(super_store['City'].value_counts().head(50)).index)
plt.xticks(rotation=90)
plt.show()


print (super_store['State'].value_counts())
plt.figure(figsize=(15,8))
sns.countplot(x=super_store['State'])
plt.xticks(rotation=90)
plt.show()


print (super_store['Category'].value_counts())
plt.figure(figsize=(10,6))
sns.countplot(x=super_store['Category'])
plt.show()


print (super_store['Sub-Category'].value_counts())
plt.figure(figsize=(12,6))
sns.countplot(x=super_store['Sub-Category'])
plt.xticks(rotation=90)
plt.show()



plt.figure(figsize=(12,6))
plt.pie(super_store['Category'].value_counts(), labels=super_store['Category'].value_counts().index, startangle=180, radius=1)
plt.title('Main category of operation')
plt.show()
print (super_store['Category'].value_counts())


plt.figure(figsize=(12,6))
plt.pie(super_store['Sub-Category'].value_counts(), labels=super_store['Sub-Category'].value_counts().index, startangle=180, radius=1)
plt.show()
print (super_store['Sub-Category'].value_counts())


#MOST PROFITABLE CATEGORIES

dfprofit = dataset.groupby('Category')['Profit'].sum().reset_index()
print(dfprofit)
plt.figure(figsize=(5,5))
labels=dfprofit['Category'].unique()
plt.pie(dfprofit['Profit'],autopct='%1.1f%%',labels=labels,explode=(0.02,0.02,0.02))

plt.title('Distribution of profits categorywise',size=20)
plt.show()

#MOST PROFITABLE PRODUCTS AND VISUALISING IT

dftop10_items = dataset.groupby('Sub-Category')['Profit'].sum().reset_index().sort_values(by='Profit',ascending=False)
dftop10_items.reset_index(drop=True,inplace=True)
dftop10_items=dftop10_items.head(10)
dftop10_items
sns.catplot('Sub-Category','Profit',data=dftop10_items,kind='bar',aspect=1.5,height=9,palette='ch:2.5,-.2,dark=.3')
plt.title('Top 10 profitable products',size=20)
plt.xticks(size=15)
plt.yticks(size=15)
plt.ylabel('Cumulative profit',size=18)
plt.xlabel('Products',size=18)

#TOP PROFITABLE CITIES

dftop10_cities = dataset.groupby('City')['Profit'].sum().reset_index().sort_values(by='Profit',ascending=False)

dftop10_cities = dftop10_cities.head(10)
dftop10_cities
sns.catplot('City','Profit',data=dftop10_cities,kind='bar',aspect=2,height=8,palette='RdBu')
plt.title('Top 10 cities with profit inflow',size=25)
plt.xticks(size=15)
plt.yticks(size=15)
plt.ylabel('Cumulative profit',size=18)
plt.xlabel('City',size=18)

plt.show()


""""CONCLUSION
From above Data Visualization we can conclude as follow:
Data Quality: Good quality data with no need for data preprocessing. No null values in Data set.
Sales: 22,97,201
Profit: 2,86,397
'Standard Class' accounts for the majority of profit.
'HomeOffice' segment generates least sale.
In central region Furniture incures loss.
'Florida', 'Oregon', 'Arizona', 'Illinois', 'Texas', 'Pennsylvania', 'Tennessee', 'North Carlina', 'Colorado' and 'Ohio' have noticeably less Profit.




