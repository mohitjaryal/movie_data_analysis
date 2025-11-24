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