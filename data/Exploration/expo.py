import pandas as pd

# Load CSV
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Basic exploration
print('First 10 rows :',df.head(10))
print('Info :',df.info())
print(df.describe())
print(df.columns)