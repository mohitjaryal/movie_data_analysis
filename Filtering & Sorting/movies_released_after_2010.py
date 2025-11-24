import pandas as pd

# Load CSV
df = pd.read_csv('data/tmdb_5000_movies.csv')

# converting releasedate to datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# filtering movies after 2010
movies_after_2010 = df[df['release_date'].dt.year > 2010]

# displaying results
print('Movies released after 2010 : \n',movies_after_2010[['title','release_date']])

# total no. of movies releaded 