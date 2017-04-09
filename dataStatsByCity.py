"""analysis of numerical fields"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1 = pd.read_csv("family_comp1_final2.csv")
# 2 adults, 0 children, 1 room
df2 = pd.read_csv("family_comp2_final2.csv")
# 2 adults, 1-3 children, 1-2 rooms
df3 = pd.read_csv("family_comp3_final2.csv")
# 1 adult, 0 children, 1 room
df4 = pd.read_csv("family_comp4_final2.csv")
# 1 adult, 1-3 children, 1-2 rooms



temp1 = df1.describe()
temp2 = df2.describe()
temp3 = df3.describe()
temp4 = df4.describe()
temp1.to_csv("dataStatsFam1.csv")
temp2.to_csv("dataStatsFam2.csv")
temp3.to_csv("dataStatsFam3.csv")
temp4.to_csv("dataStatsFam4.csv")
    
