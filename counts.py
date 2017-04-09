import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1 = pd.read_csv("DataSampleFamilyComp1.csv")
# 2 adults, 0 children, 1 room
df2 = pd.read_csv("DataSampleFamilyComp2.csv")
# 2 adults, 1-3 children, 1-2 rooms
df3 = pd.read_csv("DataSampleFamilyComp3.csv")
# 1 adult, 0 children, 1 room
df4 = pd.read_csv("DataSampleFamilyComp4.csv")
# 1 adult, 1-3 children, 1-2 rooms
familyComps = [df1,df2,df3,df4]

for family in familyComps:
    print ("\n" + "Size = " + str(len(family.index)) + "\n")
    print family['prop_starrating'].value_counts()
    print family['user_location_city'].value_counts()
    print family['is_package'].value_counts()
    print family['is_booking'].value_counts()
    print family['is_mobile'].value_counts()
    print ("________________________________________")
