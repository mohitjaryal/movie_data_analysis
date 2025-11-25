# average profit 

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Clean data
df['budget'] = pd.to_numeric(df['budget'], errors='coerce').fillna(0)
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce').fillna(0)

# Compute profit
profit = df['revenue'].to_numpy() - df['budget'].to_numpy()

# Average profit of only profitable movies
avg_profit = np.mean(profit[profit > 0])

print("Average profit among profitable movies:", avg_profit)
