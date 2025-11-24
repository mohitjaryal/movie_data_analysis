import pandas as pd

# Load CSV
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Converting release_date to datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')