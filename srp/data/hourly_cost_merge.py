import pandas as pd

df = pd.read_csv('hourlyCost7_14_2025_to_8_13_2025.csv')
df1 = pd.read_csv('hourlyCost8_14_2025_to_9_13_2025.csv')
df2 = pd.read_csv('hourlyCost9_14_2025_to_9_26_2025.csv')
df_merged = pd.concat([df, df1, df2], ignore_index=True, sort=False)
df_merged.to_csv('hourlyCost7_14_2025_to_9_26_2025.csv', index=False)
