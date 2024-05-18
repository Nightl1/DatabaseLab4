from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['DatabaseLab4']  
grades_collection = db['Grades']

# Class IDs
class_ids = [149, 350]

# Dictionary to save results for each class_id
class_result = {}

# Iterate over each class_id
for class_id in class_ids:
    pipeline = [
        {
            '$match': {'class_id': class_id}
        },
        {
            '$project': {
                'class_id': 1,
                'scores': 1
            }
        },
        {
            '$unwind': '$scores'
        },
        {
            '$group': {
                '_id': '$scores.type',
                'avg_score': {'$avg': '$scores.score'}
            }
        }
    ]

    result = list(grades_collection.aggregate(pipeline))

    # Convert to DataFrame
    result_df = pd.DataFrame(result)

    # Add class_id field
    result_df['class_id'] = class_id

    # Save the answer in class_result
    class_result[class_id] = result_df

# Define colors for each evaluation type
color_dict = {
    'quiz': 'darkblue',
    'homework': 'lightgreen',
    'exam': 'royalblue'
}

# Create subplots
fig, axs = plt.subplots(1, len(class_ids), figsize=(16, 3))

# bar graphs for each class_id
for i, class_id in enumerate(class_ids):
    result_df = class_result[class_id].sort_values(by='_id', key=lambda x: x.map({'quiz': 0, 'homework': 1, 'exam': 2}))

    colors = [color_dict.get(evaluation_type, 'skyblue') for evaluation_type in result_df['_id']]

    # reducing spaces between bars
    axs[i].barh(result_df['_id'], result_df['avg_score'], color=colors, align='edge', height=0.5, edgecolor='black', linewidth=0.5)
    axs[i].set_title(f'Class ID {class_id}')
    axs[i].invert_yaxis()
    
    # Add the liens in x axises
    axs[i].grid(axis='x', linestyle='--', color='blue')

plt.tight_layout()
plt.savefig('averageScoresClass.png') 
plt.show()
