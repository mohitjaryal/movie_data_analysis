import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('data/tmdb_5000_movies.csv')

# data cleaning
df['budget'] = pd.to_numeric(df['budget'], errors='coerce').fillna(df['budget'].mean())
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce').fillna(df['revenue'].mean())

# calculating profit
profit = df['revenue'].to_numpy - df['budget'].to_numpy() 

# profitable movies
profitable_movies = np.sum(profit > 0)
total_movies = len(profit)
percentage_profitable = (profitable_movies / total_movies) * 100

# displaying result
print(f"Percentage of profitable movies: {percentage_profitable:.2f}%")