# Calculate average rating per year 
import pandas as pd

# Load CSV
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Convert release_date to datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Extract release year
df['release_year'] = df['release_date'].dt.year

# Dropping missing years 
df = df.dropna(subset=['release_year', 'vote_average'])

# Group by release_year and calculate average rating
avg_rating_per_year = df.groupby('release_year')['vote_average'].mean().round(2)

# Display the result
print("Average rating per year:\n", avg_rating_per_year)
