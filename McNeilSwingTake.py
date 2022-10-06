#!/usr/bin/env python
# coding: utf-8

# ## McNeil Swing/Take
# This code provides visualizations for two of the changes Jeff McNeil's made in the 2022 MLB Sesason 
# 
# 1. Shows his current standing among Hitters who have produced the most Run Value In the Shadow Zone
# 
# 2. Shows his YoY Change in all Four Attack Zones 

# In[50]:


#Importing Packages 
import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[51]:


#Importing 2021 and 2022 Swing Take Datasets
SwingTake2021= pd.read_csv("swing-take (15).csv")
SwingTake2022= pd.read_csv("swing-take (14).csv")


# #### Basic EDA (Exploratory Data Analysis) 

# In[52]:


SwingTake2022.info()


# In[53]:


#Creating a new Column of merged name 
SwingTake2022['name'] = SwingTake2022[' first_name'] + "_" + SwingTake2022['last_name']
SwingTake2021['name'] = SwingTake2021[' first_name'] + "_" + SwingTake2021['last_name']


# In[54]:


#Dropping Unnecessary Columns 
SwingTake2021 = SwingTake2021.drop(['last_name',' first_name',"year",'pa','pitches'], axis =1)
SwingTake2022 = SwingTake2022.drop(['last_name',' first_name',"year",'pa','pitches'], axis =1)


# In[55]:


Shadow2021= SwingTake2021.drop(['team_id','runs_all','runs_heart','runs_chase','runs_waste'], axis =1)
Shadow2022= SwingTake2022.drop(['team_id','runs_all','runs_heart','runs_chase','runs_waste'], axis =1)


# In[56]:


#Using this next few lines to create a backup for Team analysis and dropping unnecessary cols from that, should put this earlier or later 
test1 = SwingTake2021[:]
test2 = SwingTake2022[:]


# In[57]:


#Merging the two DB, based on the date 
Shadow = Shadow2021.merge(Shadow2022, on ='player_id')
Shadow


# In[58]:


#Quick Calc to Create Data Viz
Shadow['difference'] = abs(Shadow['runs_shadow_x']) - abs(Shadow['runs_shadow_y'])
Shadow


# In[59]:


top5 = Shadow.sort_values(by=['difference'], ascending = False)
top15 = top5.head(15)
top15


# In[60]:


top15.info()


# In[61]:


McNeil.head()


# In[62]:


trying = top15.drop(['player_id','runs_shadow_x','name_x','runs_shadow_y'], axis =1)
trying


# In[63]:


#Setting Chart Style
sns.set_style('darkgrid')

#Naming the title and axis labels
plt.figure(figsize=(25,10))
sns.barplot(x = 'name_y', y= 'difference', color ="#87CEFA" , data = trying) #Want McNeil to be orange
plt.title("Biggest Improvers in The Shadow Zone (2021-2022)",fontsize = 30)
plt.ylabel('Runs', fontsize = 20)
plt.xlabel('Player', fontsize = 15)

#Work-around to highlight McNeil's column
rectangle = plt.Rectangle((1.5,0,5),1,26, fc='#ffdab9')
plt.gca().add_patch(rectangle)

plt.show()

plt.savefig('RunsByInning.png')


# # Plot that shows Jeff McNeil's Change in the Attack Zones YoY

# In[64]:


#Reading the csv
Years = pd.read_csv('Years.csv')


# In[65]:


#Splicing the Data
Years = Years.sort_values(by=['Zone'], ascending = True)
McNeilChase= Years.head(5)
McNeilHeart= Years[5:10]
McNeilShadow= Years[10:15]
McNeilWaste= Years[15:20]
#Can i make this a defintion


# In[66]:


#Data Cleaning and Splicing 
McNeilChase = McNeilChase.sort_values(by=['Year'], ascending = True)
xChaseAxis = McNeilChase['Year']
yChaseAxis = McNeilChase['Run']
McNeilChase


# In[67]:


McNeilHeart = McNeilHeart.sort_values(by=['Year'], ascending = True)
xHeartAxis = McNeilHeart['Year']
yHeartAxis = McNeilHeart['Run']
McNeilHeart


# In[68]:


McNeilShadow = McNeilShadow.sort_values(by=['Year'], ascending = True)
xShadowAxis = McNeilShadow['Year']
yShadowAxis = McNeilShadow['Run']
McNeilShadow


# In[69]:


McNeilWaste = McNeilWaste.sort_values(by=['Year'], ascending = True)
xWasteAxis = McNeilWaste['Year']
yWasteAxis = McNeilWaste['Run']
McNeilWaste


# In[70]:


'''
First split: Plotting all of the line graphs

Second Split: making the legend in the lower left

Third Split: Title and axis labels 

Fourth Split: Ensuring that the x axis labels won't have decimals

Fifth Split: Displaying the plot

'''

plt.figure(figsize = (15,8))
plt.plot(xChaseAxis,yChaseAxis, '-.', color='red', marker ='o')
plt.plot(xHeartAxis,yHeartAxis,'-.', color='green', marker ='o')
plt.plot(xShadowAxis,yShadowAxis, '-.', color='blue', marker ='o')
plt.plot(xWasteAxis,yWasteAxis, '-.', color='orange', marker ='o')


plt.legend(('Chase', 'Heart', 'Shadow','Waste'),
           loc='lower left', shadow=True, fontsize =20)

plt.title("Jeff McNeil's Swing/Take Profile Throughout the Years", fontsize =25)
plt.xlabel('Year', fontsize = 20)
plt.ylabel('Runs', fontsize = 20)


x_ticks = (2018,2019,2020,2021,2022)
x_labels = (2018,2019,2020,2021,2022)
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.xlim (2018,2022)
plt.xticks()


plt.show()
plt.savefig('McNeilSwingTake.png')


# In[ ]:


#Defintion Test
def splice(Years):
    counter3 = 0
    while counter3 <= 20:
        appender = []
        counter2 = 0
        counter3 = 5
        z= Years[counter2: counter3]
        counter2 += 4
        counter3 += 4
        appender = appender.append(z)
    return z, appender
print(splice(Years))


# In[ ]:





# In[53]:





# In[ ]:





# In[ ]:




