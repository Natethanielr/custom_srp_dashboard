# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import daily cost csv
df = pd.read_csv('dailyCost7_14_2025_to_8_12_2025.csv')
# import hourly cost csv
df1 = pd.read_csv('hourlyCost7_14_2025_to_8_5_2025.csv')
# convert usage date to pandas datetime
df['Usage date'] = pd.to_datetime(df['Usage date'])
# remove $ and covert to float
df['Total cost'] = df['Total cost'].replace(
    {'\\$': '', ',': ''}, regex=True).astype(float)
# create a new column with the day of week
df['Day of week'] = df['Usage date'].dt.day_name()
