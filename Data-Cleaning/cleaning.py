import pandas as pd

# Load CSV
df = pd.read_csv('data/tmdb_5000_movies.csv')

# Converting release date to datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
print('Data after converting to datetime :\n',df)

# filling important values
df['budget'] = df['budget'].fillna(0)
df['revenue'] = df['revenue'].fillna(0)

