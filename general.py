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
#import matplotlib
#import matplotlib
#matplotlib.use('Agg')
#matplotlib.style.use('ggplot')
#import matplotlib as plt
#print matplotlib.__version__

#user_location_region
df_fam1 = pd.read_csv("family_comp3_final3.csv")
print df_fam1['is_package'].value_counts()

"""
df_unclean = pd.read_csv("dataSampled.csv", header=0, na_values=['NULL'])

print df_unclean.shape

#drop doplicates
df_no_duplicates = df_unclean.drop_duplicates()
print df_no_duplicates.shape 

df_eliminate_null = df_no_duplicates.dropna()

#Eliminate rows with Null. 
print df_eliminate_null.shape

#df_eliminate_null.to_csv("cleanedData.csv")

#most popular dates in the cleaned data set
print df_eliminate_null['srch_ci'].value_counts()"""
"""
df_ = pd.read_csv("data_cleaned_couples.csv")
print df_.shape
print df_['is_package'].value_counts()
print df_['srch_children_cnt'].value_counts()
print df_['is_booking'].value_counts()
print df_['prop_starrating'].value_counts()



#df_ = pd.read_csv("cleanedData.csv")
df_ = pd.read_csv("cleanedData.csv")
#families with 2 parents, 1-3 children
df_fam_comp2 = pd.read_csv("family_comp2.csv")
print df_fam_comp2.shape
print df_fam_comp2['is_package'].value_counts()
print df_fam_comp2['srch_children_cnt'].value_counts()
print df_fam_comp2['is_booking'].value_counts()
print df_fam_comp2['prop_starrating'].value_counts()
print df_fam_comp2['user_location_city'].value_counts()  

#0 children, 2 adults, 1-2 rooma
df_fam_comp3 = pd.read_csv("family_comp3.csv")
print df_fam_comp3.shape
print df_fam_comp3['is_package'].value_counts()
print df_fam_comp3['srch_children_cnt'].value_counts()
print df_fam_comp3['is_booking'].value_counts()
print df_fam_comp3['prop_starrating'].value_counts()

df_fam_comp4 = pd.read_csv("family_comp4.csv")
print df_fam_comp4.shape
print df_fam_comp4['is_package'].value_counts()
print df_fam_comp4['srch_children_cnt'].value_counts()
print df_fam_comp4['is_booking'].value_counts()
print df_fam_comp4['prop_starrating'].value_counts()
fig_fam_comp4 = df_fam_comp4['prop_starrating'].hist(bins=50)
fig_fam_comp4.set_xlabel("Major chain")
fig_fam_comp4.set_ylabel("Ratings")
temp2 = fig_fam_comp4.get_figure()
temp2.savefig("famComp1-ratingsHotelChain.png")




df_ = pd.read_csv("cleanedData.csv")
print df_['user_location_city'].value_counts()


#print df_.shape
#print df['srch_ci'].value_counts()

#print df_['is_package'].value_counts()

#print df_['srch_children_cnt'].value_counts()

#Data stats: 

#stats = df_.describe()
#stats.to_csv('cleanedDataStats.csv')

fig = df_['is_booking'].hist(bins=50)
fig.set_title("Packages and Booking")
fig.set_xlabel("ratings")
fig.set_ylabel("Number of users")
temp = fig.get_figure()
temp.savefig("bookedAndPackage.png")"""

"""




#df = pd.read_csv("dataSampled.csv") #Reading the dataset in a dataframe using Pandas
#print df.head(10) 

fig = df['srch_adults_cnt'].hist(bins=50)
fig.set_title("Distribution of number of adults/room")
fig.set_xlabel("Number of Adults per room")
fig.set_ylabel("Number of users")
temp = fig.get_figure()
temp.savefig("adult.png")


fig = df_['prop_starrating'].hist(bins=50)
fig.set_title("Distribution of ratings")
fig.set_xlabel("Ratings")
fig.set_ylabel("Number of users")
temp = fig.get_figure()
temp.savefig("ratings.png")


fig3 = df.boxplot(column='prop_starrating', by='srch_children_cnt')
fig3.set_xlabel("Number of Children")
fig3.set_ylabel("Ratings")
temp = fig3.get_figure()
temp.savefig("ratingsByChildren.png")

fig1 = df.boxplot(column='prop_starrating', by='srch_adults_cnt')
fig1.set_xlabel("Number of Adults")
fig1.set_ylabel("Ratings")
temp1 = fig1.get_figure()
temp1.savefig("ratingsByAdult.png")

fig2 = df.boxplot(column='prop_starrating', by='prop_is_branded')
fig2.set_xlabel("Major chain")
fig2.set_ylabel("Ratings")
temp2 = fig2.get_figure()
temp2.savefig("ratingsHotelChain.png")"""

#fig = df.boxplot(column='is_booking', by='is_mobile')


#temp = fig.get_figure()

#temp.savefig("haha.png")

#fig = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))

#temp = fig.cumsum()

#test = plt.get_figure() 

"""
test = pd.DataFrame(np.random.rand(50, 2),  columns=['is_booking', 'prop_starrating'])
fig = df.plot.scatter(x='is_booking', y='prop_starrating')

haha = fig.get_figure()
haha.savefig("test.png")"""


#get summary of numerical variables

#print df['user_location_city'].value_counts()
"""
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()


df = pd.DataFrame(np.random.randn(1000, 2), columns=[x, y]).cumsum()

df[x] = pd.Series(list(range(len(df))))

fig.savefig("test.png")"""




 #ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

#ts = ts.cumsum()

#ts.plot()




"""
print df.describe()

temp = df.describe()



temp.to_csv("dataStats.csv")
"""



#temp.to_csv('test.csv')
#temp = df.groupby('name')['prop'].describe().reset_index()
"""
temp = df.describe().reset_index()

newdf = temp.pivot(index='name',columns='level_1',values=0)

newdf.columns.name = ''   #This is needed so that the name of the columns is not `'level_1'` .

newdf.to_csv("dataStats.csv")"""




































