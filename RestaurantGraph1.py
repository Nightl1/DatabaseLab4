import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv('sample_restaurants.restaurants.csv')

# Create DF for Polish restaurants
polish_restaurants = df[df['cuisine'] == 'Polish']
polish_grouped = polish_restaurants.groupby('borough').size().reset_index(name='total')

# Create DF for Italian restaurants
italian_restaurants = df[df['cuisine'] == 'Italian']
italian_grouped = italian_restaurants.groupby('borough').size().reset_index(name='total')

# Sort Italian restaurants by total number
italian_grouped = italian_grouped.sort_values(by='total', ascending=False)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))

# Polish cuisine
axes[0].bar(polish_grouped['borough'], polish_grouped['total'], color='blue')
axes[0].set_title('Polish')
axes[0].tick_params(axis='x', rotation=45)

# Italian cuisine
axes[1].bar(italian_grouped['borough'], italian_grouped['total'], color='blue')
axes[1].set_title('Italian')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('boroughPerTypeofCuisine.png')  # Save the plot as PNG
plt.show()
