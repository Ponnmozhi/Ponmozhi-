# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the example dataset (tips from seaborn)
import seaborn as sns
tips = sns.load_dataset('tips')
print(tips.head())
# Basic Data Manipulation
print(tips.info())
print(tips.describe())
# Data Filtering
tips_filtered = tips[tips['tip'] > 5]
print(tips_filtered.head())

# Data Sorting
tips_sorted = tips.sort_values(by='total_bill', ascending=False)
print(tips_sorted.head())

# Data Grouping
tips_grouped = tips.groupby('sex')['tip'].mean()
print(tips_grouped)

# Data Merging
tips_merged = pd.merge(tips, tips.groupby('sex')['tip'].mean().reset_index(), on='sex')
print(tips_merged.head())

# Data Handling Missing Values
tips_missing = tips.copy()
tips_missing.loc[0, 'tip'] = np.nan
print(tips_missing.head())
print(tips_missing.isnull().sum())

# Data Visualization
plt.figure(figsize=(8,6))
plt.scatter(tips['total_bill'], tips['tip'])
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Total Bill vs Tip')
plt.show()

# Intermediate Data Manipulation
tips_pivot = tips.pivot_table(index='sex', columns='smoker', values='tip', aggfunc='mean')
print(tips_pivot)

# Melting Data
tips_melted = pd.melt(tips, id_vars=['sex', 'smoker'], value_vars=['total_bill', 'tip'])
print(tips_melted.head())



