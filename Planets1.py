import pandas as pd
from pymongo import MongoClient

# Connect with db
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

# Execute the list
planets_data = list(planets_collection.aggregate(pipeline))

# Replace unique _id
for idx, planet in enumerate(planets_data):
    planet['_id'] = idx + 1

# Create column names
df = pd.DataFrame(planets_data, columns=['_id', 'name', 'minTemp', 'maxTemp', 'avgTemp'])

# show the result
print(df.to_markdown(index=False))
