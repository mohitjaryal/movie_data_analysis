# stat of budget

import numpy as np
import pandas as pd

# loading dataset
df = pd.read_csv('data/tmdb_5000_movies.csv')

# data cleaning
df['budget'] = pd.to_numeric(df['budget'], errors='coerce').fillna(df['budget'].mean())

# converting to numpy array
revenue = ['budget'].to_numpy()

# Statistics
print("Budget Statistics:")
print("Mean:", np.mean(revenue))
print("Median:", np.median(revenue))
print("Standard Deviation:", np.std(revenue))
print("Min:", np.min(revenue))
print("Max:", np.max(revenue))