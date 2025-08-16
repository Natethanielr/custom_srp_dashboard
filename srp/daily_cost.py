# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#Import csv
df = pd.read_csv('dailyCost7_14_2025_to_8_4_2025.csv')
#Convert to datetime
df['Usage date'] = pd.to_datetime(df['Usage date'])
#Convery cost to float
df['Total cost'] = df['Total cost'].replace({'\\$': '', ',': ''}, regex=True).astype(float)
#Create column with the days of the week
df['Day of week'] = df['Usage date'].dt.day_name()

print(df.head())
# Create a lists to color code week/weekdays
colors = ['red' if day in ['Saturday', 'Sunday'] else 'blue' for day in df['Day of week']]

#Plot the cost over time
fig, ax = plt.subplots(figsize = (10,5))
ax.bar(df['Usage date'], df['Total cost'], edgecolor = colors, label = 'Total Cost')
#ax.plot(df['Usage date'], df['Total cost'],'k')
ax1 = ax.twinx()
ax1.plot(df['Usage date'], df['High temperature (F)'], 'k', ls = 'dotted', label = 'High temperature') 
ax.set_xlabel('Usage date')
ax.set_ylabel('Cost $')
ax1.set_ylabel('Temperature')
ax.legend()
ax1.legend()
