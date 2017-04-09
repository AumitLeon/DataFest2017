import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import matplotlib as plt

df = pd.read_csv("dataSampled.csv") #Reading the dataset in a dataframe using Pandas
#print df.head(10) 


#get summary of numerical variables

print df.describe()