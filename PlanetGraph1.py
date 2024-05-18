import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt

# Connect with the database
client = MongoClient('mongodb://localhost:27017/')
db = client['DatabaseLab4']
planets_collection = db['Planets']

pipeline = [
    {
        '$project': {
            '_id': 1,
            'name': 1,
            'orderFromSun': 1,
            'minTemp': '$surfaceTemperatureC.min',
            'maxTemp': '$surfaceTemperatureC.max',
            'avgTemp': {
                '$ifNull': [
                    '$surfaceTemperatureC.mean',
                    {
                        '$cond': {
                            'if': {
                                '$and': [
                                    {'$ne': ['$surfaceTemperatureC.min', None]},
                                    {'$ne': ['$surfaceTemperatureC.max', None]}
                                ]
                            },
                            'then': {
                                '$divide': [
                                    {'$add': ['$surfaceTemperatureC.min', '$surfaceTemperatureC.max']},
                                    2
                                ]
                            },
                            'else': None
                        }
                    }
                ]
            }
        }
    },
    { 
        '$sort': {'orderFromSun': 1}
    }
]

planets_data = list(planets_collection.aggregate(pipeline))

# Replace unique _id
for idx, planet in enumerate(planets_data):
    planet['_id'] = idx + 1

# Create DataFrame
df = pd.DataFrame(planets_data, columns=['_id', 'name', 'minTemp', 'maxTemp', 'avgTemp'])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['name'], df['minTemp'], color='blue', label='Min Temperature')
plt.plot(df['name'], df['maxTemp'], color='green', label='Max Temperature')
plt.plot(df['name'], df['avgTemp'], color='orange', label='Avg Temperature')
plt.xlabel('Planet')
plt.ylabel('Surface Temperature (°C)')
plt.title('Surface Temperature of Planets')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout() # adjust size based on window adjusting
plt.savefig('surfaceTemperatureofPlanetsinSolorSystem_linear.png')
plt.show()
