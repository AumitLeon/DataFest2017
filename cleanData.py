"""clean data"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import matplotlib as plt

df = pd.read_csv("dataSampled.csv") #Reading the dataset in a dataframe using Pandas
#If the data contains missing data indicated by 'NA', you can read the data in as follows:


#(rows x column)
print df.shape 

df_unclean = pd.read_csv("dataSampled.csv", header=0, na_values=['NULL'])

print df_unclean.shape

#drop doplicates
df_no_duplicates = df_unclean.drop_duplicates()
print df_no_duplicates.shape 
#Drop nulls
df_eliminate_null = df_no_duplicates.dropna()

print df_eliminate_null.shape
df_eliminate_null.to_csv("cleanedData.csv")


"""
#temp.to_csv('test.csv')
#temp = df.groupby('name')['prop'].describe().reset_index()

temp = df.describe().reset_index()

newdf = temp.pivot(index='name',columns='level_1',values=0)

newdf.columns.name = ''   #This is needed so that the name of the columns is not `'level_1'` .

newdf.to_csv("dataStats.csv")"""