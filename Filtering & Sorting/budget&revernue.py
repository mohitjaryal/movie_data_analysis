# Filter movies with budget > 100 million and revenue > 200 million.

import pandas as pd

# Load CSV
df = pd.read_csv('data/tmdb_5000_movies.csv')

#filling missing numeric values with mean()
df['budget'] = df['budget'].fillna(df['budget'].mean())
df['revenue'] = df['revenue'].fillna(df['budget'].mean())


# Convert to numeric 
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')

# Filtering movies with budget > 100 million and revenue > 200 million
movies = df[(df['budget'] > 100000000) & (df['revenue'] > 200000000)]

# displaying 
print('Movies with budget > 100 million and revenue > 200 million :\n',movies[['title','budget','revenue']])

# total count
print("\nTotal movies meeting the criteria:", len(movies))