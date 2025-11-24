import pandas as pd


# Load CSV
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Basic exploration

# first 10 rows
print('First 10 rows :\n',df.head(10))

# columns name
print('Column names :\n',df.columns)

# checking data types
print('Info :',df.info())

# checking missing values 