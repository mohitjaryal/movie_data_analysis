# Find top 10 highest revenue movies

import pandas as pd

# Load CSV
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Fill missing revenue with 0 (optional, if needed)
df['revenue'] = df['revenue'].fillna(0)

# Sorting revenue descending and get top 10
top_10_revenue = df.sort_values('revenue', ascending=False).head(10)

# Display movie title and revenue
print("Top 10 highest revenue movies :\n",top_10_revenue[['title', 'revenue']])
