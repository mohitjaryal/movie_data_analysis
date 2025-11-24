import pandas as pd

# Load CSV
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Filling the missing values
df['vote_average'] = df['vote_average'].fillna(df['vote_average']).mean()
df['vote_count'] = df['vote_count'].fillna(df['vote_count']).mean()

# min vote count to filter
min_votes = 50
popular_movies = df[df['vote_count'] >= min_votes]

# sorting to get top 10 movies
top_10_movies = popular_movies.sort_values('vote_average',ascending=False).head(10)
print('Top 10 popular movies :\n',top_10_movies['title', 'vote_average', 'vote_count'])