import pandas as pd

# Read CSV file
df = pd.read_csv('sample_restaurants.restaurants.csv')

# Create DF for Polish restaurants
polish_restaurants = df[df['cuisine'] == 'Polish']
polish_grouped = polish_restaurants.groupby('borough').size().reset_index(name='total')

# Create DF for Italian restaurants
italian_restaurants = df[df['cuisine'] == 'Italian']
italian_grouped = italian_restaurants.groupby('borough').size().reset_index(name='total')

# Print DF
print("Total number of Polish cuisine restaurants grouped by borough:")
print(polish_grouped)

# Sort by big to small
italian_grouped = italian_grouped.sort_values(by='total', ascending=False)

print("\nTotal number of Italian cuisine restaurants grouped by borough:")
print(italian_grouped)
