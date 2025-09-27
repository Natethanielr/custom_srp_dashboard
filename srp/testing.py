import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import daily cost csv
df = pd.read_csv('cost_data/dailyCost7_14_2025_to_9_26_2025.csv')
# drop last combined row
# df = df.drop(df.index[-1])
df = df.dropna(subset=['Usage date'])
# import hourly cost csv
df1 = pd.read_csv('cost_data/hourlyCost7_14_2025_to_9_26_2025.csv')
# convert usage date to pandas datetime
df['Usage date'] = pd.to_datetime(df['Usage date'])
# remove $ and covert to float
df['Total cost'] = df['Total cost'].replace(
    {'\\$': '', ',': ''}, regex=True).astype(float)
# create a new column with the day of week
df['Day of week'] = df['Usage date'].dt.day_name()
print(df.dtypes)

# create a list that assignes colors for the weekdays/weekends for Day of Week
colors = ['red' if day in ['Saturday', 'Sunday']
          else 'blue' for day in df['Day of week']]
# initate figure and axis for plotting
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df['Usage date'], df['Total cost'], edgecolor=colors,
       color='steelblue', label='Total Cost')
# create a secondary axis on the same figure for the temperature
ax1 = ax.twinx()
ax1.plot(df['Usage date'], df['High temperature (F)'],
         'k', ls='dotted', label='High temperature')
ax.set_xlabel('Usage date')
ax.set_ylabel('Cost $')
# ax.set_ylim(0,8)
ax1.set_ylabel('Temperature')
ax1.set_ylim(20, 120)
ax.legend()
ax1.legend()
plt.show()
print(df.tail())
