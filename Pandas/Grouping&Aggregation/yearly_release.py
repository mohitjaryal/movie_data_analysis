# Find no. of movies released per year

import pandas as pd

# Load CSV
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Converting release_date to datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# extracting release year
df['release_date'] = df['release_date'].dt.year

# counting no. of mivies per year
movies_per_year = df['release_date'].value_counts().sort_index()

# displaying 
print("Number of movies released per year:\n", movies_per_year)