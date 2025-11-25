# stat of budget

import numpy as np
import pandas as pd

# loading dataset
df = pd.read_csv('data/tmdb_5000_movies.csv')

# data cleaning
df['budget'] = pd.to_numeric(df['budget'], errors='coerce').fillna(df['budget'].mean())

# converting to numpy array
budget = df['budget'].to_numpy()

# Statistics
print("Budget Statistics:")
print("Mean:", np.mean(budget))
print("Median:", np.median(budget))
print("Standard Deviation:", np.std(budget))
print("Min:", np.min(budget))
print("Max:", np.max(budget))