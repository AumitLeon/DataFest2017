#General purpose script
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
"""import matplotlib.pyplot as plt
plt.use('Agg')
plt.style.use('ggplot')"""

#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df_fam1 = pd.read_csv("family_comp1_parsedcity.csv")
df_fam2 = pd.read_csv("family_comp2_parsedcity.csv")
df_fam3 = pd.read_csv("family_comp3_parsedcity.csv")
df_fam4 = pd.read_csv("family_comp4_parsedcity.csv")


#updated = df_.loc[(df_['user_location_city'] == 'NEW YORK') & (df_['user_location_city'] == 'BOSTON')]
#df_[ (df_.user_location_city=='NEW YORK') ]['income'] = '60'
#df_.to_csv('byCity.csv') 

#df_['income'] = df_['NEW YORK'].map({'income': 600000})
"""
df_fam1.loc[df_fam1['user_location_city'] == "LOS ANGELES", 'income'] = 54510
df_fam1.loc[df_fam1['user_location_city'] == "HOUSTON", 'income'] = 61465
df_fam1.loc[df_fam1['user_location_city'] == "CHICAGO", 'income'] = 63153
df_fam1.loc[df_fam1['user_location_city'] == "CALGARY", 'income'] = 101260
df_fam1.loc[df_fam1['user_location_city'] == "BROOKLYN", 'income'] = 66739
df_fam1.loc[df_fam1['user_location_city'] == "SAN FRANCISCO", 'income'] = 88518
df_fam1.loc[df_fam1['user_location_city'] == "SEATTLE", 'income'] = 75331
df_fam1.loc[df_fam1['user_location_city'] == "MIAMI", 'income'] = 46946
df_fam1.loc[df_fam1['user_location_city'] == "VANCOUVER", 'income'] = 71140
df_fam1.loc[df_fam1['user_location_city'] == "MONTREAL", 'income'] = 75010
df_fam1.loc[df_fam1['user_location_city'] == "SAN JOSE", 'income'] = 101980
df_fam1.loc[df_fam1['user_location_city'] == "DENVER", 'income'] = 70283
df_fam1.loc[df_fam1['user_location_city'] == "ATLANTA", 'income'] = 60219

df_fam2.loc[df_fam2['user_location_city'] == "NEW YORK", 'income'] = 67602
df_fam2.loc[df_fam2['user_location_city'] == "LOS ANGELES", 'income'] = 54510
df_fam2.loc[df_fam2['user_location_city'] == "HOUSTON", 'income'] = 61465
df_fam2.loc[df_fam2['user_location_city'] == "CHICAGO", 'income'] = 63153
df_fam2.loc[df_fam2['user_location_city'] == "CALGARY", 'income'] = 101260
df_fam2.loc[df_fam2['user_location_city'] == "BROOKLYN", 'income'] = 66739
df_fam2.loc[df_fam2['user_location_city'] == "SAN FRANCISCO", 'income'] = 88518
df_fam2.loc[df_fam2['user_location_city'] == "SEATTLE", 'income'] = 75331
df_fam2.loc[df_fam2['user_location_city'] == "MIAMI", 'income'] = 46946
df_fam2.loc[df_fam2['user_location_city'] == "VANCOUVER", 'income'] = 71140
df_fam2.loc[df_fam2['user_location_city'] == "MONTREAL", 'income'] = 75010
df_fam2.loc[df_fam2['user_location_city'] == "SAN JOSE", 'income'] = 101980
df_fam2.loc[df_fam2['user_location_city'] == "DENVER", 'income'] = 70283
df_fam2.loc[df_fam2['user_location_city'] == "ATLANTA", 'income'] = 60219


df_fam3.loc[df_fam3['user_location_city'] == "NEW YORK", 'income'] = 67602
df_fam3.loc[df_fam3['user_location_city'] == "LOS ANGELES", 'income'] = 54510
df_fam3.loc[df_fam3['user_location_city'] == "HOUSTON", 'income'] = 61465
df_fam3.loc[df_fam3['user_location_city'] == "CHICAGO", 'income'] = 63153
df_fam3.loc[df_fam3['user_location_city'] == "CALGARY", 'income'] = 101260
df_fam3.loc[df_fam3['user_location_city'] == "BROOKLYN", 'income'] = 66739
df_fam3.loc[df_fam3['user_location_city'] == "SAN FRANCISCO", 'income'] = 88518
df_fam3.loc[df_fam3['user_location_city'] == "SEATTLE", 'income'] = 75331
df_fam3.loc[df_fam3['user_location_city'] == "MIAMI", 'income'] = 46946
df_fam3.loc[df_fam3['user_location_city'] == "VANCOUVER", 'income'] = 71140
df_fam3.loc[df_fam3['user_location_city'] == "MONTREAL", 'income'] = 75010
df_fam3.loc[df_fam3['user_location_city'] == "SAN JOSE", 'income'] = 101980
df_fam3.loc[df_fam3['user_location_city'] == "DENVER", 'income'] = 70283
df_fam3.loc[df_fam3['user_location_city'] == "ATLANTA", 'income'] = 60219

df_fam4.loc[df_fam4['user_location_city'] == "NEW YORK", 'income'] = 67602
df_fam4.loc[df_fam4['user_location_city'] == "LOS ANGELES", 'income'] = 54510
df_fam4.loc[df_fam4['user_location_city'] == "HOUSTON", 'income'] = 61465
df_fam4.loc[df_fam4['user_location_city'] == "CHICAGO", 'income'] = 63153
df_fam4.loc[df_fam4['user_location_city'] == "CALGARY", 'income'] = 101260
df_fam4.loc[df_fam4['user_location_city'] == "BROOKLYN", 'income'] = 66739
df_fam4.loc[df_fam4['user_location_city'] == "SAN FRANCISCO", 'income'] = 88518
df_fam4.loc[df_fam4['user_location_city'] == "SEATTLE", 'income'] = 75331
df_fam4.loc[df_fam4['user_location_city'] == "MIAMI", 'income'] = 46946
df_fam4.loc[df_fam4['user_location_city'] == "VANCOUVER", 'income'] = 71140
df_fam4.loc[df_fam4['user_location_city'] == "MONTREAL", 'income'] = 75010
df_fam4.loc[df_fam4['user_location_city'] == "SAN JOSE", 'income'] = 101980
df_fam4.loc[df_fam4['user_location_city'] == "DENVER", 'income'] = 70283
df_fam4.loc[df_fam4['user_location_city'] == "ATLANTA", 'income'] = 60219

df_fam1.to_csv('family_comp1_final.csv')
df_fam2.to_csv('family_comp2_final.csv')
df_fam3.to_csv('family_comp3_final.csv')
df_fam4.to_csv('family_comp4_final.csv')"""

df_fam1.loc[df_fam1['is_package'] == 1, 'is_package'] = "YES"
df_fam1.loc[df_fam1['is_package'] == 0, 'is_package'] = "NO"

df_fam2.loc[df_fam2['is_package'] == 1, 'is_package'] = "YES"
df_fam2.loc[df_fam2['is_package'] == 0, 'is_package'] = "NO"

df_fam3.loc[df_fam3['is_package'] == 1, 'is_package'] = "YES"
df_fam3.loc[df_fam3['is_package'] == 0, 'is_package'] = "NO"

df_fam4.loc[df_fam4['is_package'] == 1, 'is_package'] = "YES"
df_fam4.loc[df_fam4['is_package'] == 0, 'is_package'] = "NO"

#df_fam1.to_csv('family_comp1_final2.csv')
df_fam2.to_csv('family_comp2_final2.csv')
df_fam3.to_csv('family_comp3_final2.csv')
df_fam4.to_csv('family_comp4_final2.csv')