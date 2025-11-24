import pandas as pd

# Load CSV
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Filling the missing values
df['vote_average'] = df['vote_average'].fillna(df['vote_average']).mean()
