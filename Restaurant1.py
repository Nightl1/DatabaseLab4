from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['DatabaseLab4']  
restaurants_collection = db['Restaurants']  

polish_pipeline = [
    {
        '$match': {'cuisine': 'Polish'}
    },
    {
        '$group': {
            '_id': '$borough',
            'total': {'$sum': 1}
        }
    }
]

italian_pipeline = [
    {
        '$match': {'cuisine': 'Italian'}
    },
    {
        '$group': {
            '_id': '$borough',
            'total': {'$sum': 1}
        }
    },
    {
        '$sort': {'total': -1}
    }
]

# Execution for both tables
polish_results = list(restaurants_collection.aggregate(polish_pipeline))
italian_results = list(restaurants_collection.aggregate(italian_pipeline))

# put the results in DataFrames
polish_df = pd.DataFrame(polish_results)
italian_df = pd.DataFrame(italian_results)

# Print results
print("Total number of Polish cuisine restaurants grouped by borough:")
print(polish_df.to_markdown(index=False))

print("\nTotal number of Italian cuisine restaurants grouped by borough (sorted by total):")
print(italian_df.to_markdown(index=False))
