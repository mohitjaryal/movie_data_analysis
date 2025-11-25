# Find profit

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('data/tmdb_5000_movies.csv')

# data cleaning
df['budget'] = pd.to_numeric(df['budget'], errors='coerce').fillna(df['budget'].mean())
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce').fillna(df['revenue'].mean())

# calculating profit
profit = df['revenue'].to_numpy() - df['budget'].to_numpy()

print('Profit :\n',profit)

# few examples
print("Example of profit calculation:\n", df[['title', 'budget', 'revenue']].head())