import pandas as pd

# Read the CSV file
df = pd.read_csv('sample_training.grades.csv')

# dict to save results for each class_id
class_result = {}

# get class_ids
class_ids = [149, 350]

for class_id in class_ids:
    class_data = df[df['class_id'] == class_id]

    class_result[class_id] = []

    for index, row in class_data.iterrows():
        for i in range(4):
            score_type = row[f'scores[{i}].type']
            score_value = row[f'scores[{i}].score']
            class_result[class_id].append({'_id': score_type, 'avg_score': score_value})

    class_result[class_id] = pd.DataFrame(class_result[class_id])
    # Get avg score by class_id
    class_result[class_id] = class_result[class_id].groupby('_id')['avg_score'].mean().reset_index()

    # Add class_id field
    class_result[class_id]['class_id'] = class_id

for class_id, result_df in class_result.items():
    print(f"Average score per evaluation type for class_id {class_id}:")
    print(result_df[['_id', 'avg_score']])
    print()
