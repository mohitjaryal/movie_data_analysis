import pandas as pd
import numpy as np

# Create a small movie dataset
data = pd.DataFrame({
    'Movie': ['Inception', 'Titanic', 'Avengers'],
    'Rating': [8.8, 7.8, 8.1],
    'Revenue_Million': [829, 2187, 1519]
})

# Display the dataset
print("Movie Dataset:")
print(data)

# Calculate average rating using NumPy
average_rating = np.mean(data['Rating'])
print("\nAverage Movie Rating:", average_rating)

# Filter movies with rating > 8
high_rated = data[data['Rating'] > 8]
print("\nHigh Rated Movies:")
print(high_rated)
