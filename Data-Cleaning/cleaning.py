import pandas as pd

# Load CSV
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Converting release date to datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
print('Data after converting to datetime :\n',df)

# filling important values
df['vote_average'] = df['vote_average'].fillna(df['vote_average'].mean())
df['vote_count'] = df['vote_count'].fillna(df['vote_count'].mean())
