import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['DatabaseLab4']
planets_collection = db['Planets']

# Aggregation pipeline to process the data
pipeline = [
    {
        '$project': {
            '_id': 0,
            'orderFromSun': 1,
            'name': 1,
            'mainAtmosphere': 1
        }
    },
    {
        '$unwind': '$mainAtmosphere'
    },
    {
        '$addFields': {
            'color_values': {
                '$switch': {
                    'branches': [
                        {'case': {'$eq': ['$mainAtmosphere', 'CO2']}, 'then': '#00CED1'},
                        {'case': {'$eq': ['$mainAtmosphere', 'N']}, 'then': '#00FFFF'},
                        {'case': {'$eq': ['$mainAtmosphere', 'O2']}, 'then': '#228B22'},
                        {'case': {'$eq': ['$mainAtmosphere', 'Ar']}, 'then': '#00FA9A'},
                        {'case': {'$eq': ['$mainAtmosphere', 'H2']}, 'then': '#008080'},
                        {'case': {'$eq': ['$mainAtmosphere', 'He']}, 'then': '#191970'},
                        {'case': {'$eq': ['$mainAtmosphere', 'CH4']}, 'then': '#00FF00'}
                    ],
                    'default': None
                }
            }
        }
    },
    {
        '$sort': {
            'orderFromSun': 1,
            'name': 1
        }
    },
    {
        '$project': {
            '_id': '$orderFromSun',
            'orderFromSun': 1,
            'name': 1,
            'mainAtmosphere': 1,
            'color_values': 1
        }
    }
]

# Execute the aggregation pipeline
planets_data = list(planets_collection.aggregate(pipeline))

# Create a DataFrame from the aggregation results
df = pd.DataFrame(planets_data)

# Print the DataFrame
print(df)
