import numpy as np
import pandas as pd

# loading dataset
df = pd.read_csv('data/tmdb_5000_movies.csv')

# data cleaning
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce').fillna(df['revenue'].mean())

# converting to numpy array
revenue = df['revenue'].to_numpy()

# Statistics
print("📊 Revenue Statistics:")
print("Mean:", np.mean(revenue))
print("Median:", np.median(revenue))
print("Standard Deviation:", np.std(revenue))
print("Min:", np.min(revenue))
print("Max:", np.max(revenue))