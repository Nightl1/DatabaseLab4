from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['DatabaseLab4']  
grades_collection = db['Grades']
# class ids
class_ids = [149, 350]

# dictionary to save results
class_result = {}

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
        },
        {
            '$project': {
                '_id': 1,
                'avg_score': 1
            }
        }
    ]

    # Execute pipeline
    result = list(grades_collection.aggregate(pipeline))

    # Convert to DataFrame
    result_df = pd.DataFrame(result)

    # Save the nswer in class_id
    class_result[class_id] = result_df

for class_id, result_df in class_result.items():
    print(f"Average score per evaluation type for class_id {class_id}:")
    print(result_df.to_string(index=False))