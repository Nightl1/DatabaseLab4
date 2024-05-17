import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient
import pymongo

# Read the CSV file
df = pd.read_csv('sample_guides.planets.csv')

# Sort the DF by 'orderFromSun'
df.sort_values(by='orderFromSun', inplace=True)

# average surface temperature
plt.figure(figsize=(10, 6))
plt.plot(df['name'], df['surfaceTemperatureC.min'], color='blue', label='Min Temperature')
plt.plot(df['name'], df['surfaceTemperatureC.max'], color='green', label='Max Temperature')
plt.plot(df['name'], df['surfaceTemperatureC.mean'], color='orange', label='Avg Temperature')
plt.xlabel('Planet')
plt.ylabel('Surface Temperature (°C)')
plt.title('Surface Temperature of Planets')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('surfaceTemperatureofPlanetsinSolorSystem.png')  # Save the result as PNG
plt.show()
