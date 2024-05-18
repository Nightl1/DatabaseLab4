from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

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
    },
    {
        '$sort': {'total': 1}  
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
        '$sort': {'total': 1}  
    }
]

polish_results = list(restaurants_collection.aggregate(polish_pipeline))
italian_results = list(restaurants_collection.aggregate(italian_pipeline))

# put the answers in DataFrames
polish_df = pd.DataFrame(polish_results)
italian_df = pd.DataFrame(italian_results)

polish_df = polish_df[::-1]
italian_df = italian_df[::-1]

# Plot bar graphs
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Polish cuisine
axes[0].bar(polish_df['_id'], polish_df['total'], color='lightblue') 
axes[0].set_title('Polishhg')

# Italian cuisine
axes[1].bar(italian_df['_id'], italian_df['total'], color='lightblue') 
axes[1].set_title('Italian ')

axes[0].tick_params(axis='x', rotation=45)
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
