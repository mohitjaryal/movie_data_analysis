import pandas as pd

# Load CSV
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Basic exploration
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
