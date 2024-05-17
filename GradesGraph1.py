import pandas as pd
import matplotlib.pyplot as plt

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

# put colors for each bar
color_dict = {
    'homework': 'lightgreen',
    'quiz': 'darkblue',
    'exam': 'royalblue'
}

fig, axs = plt.subplots(1, len(class_ids), figsize=(12, 6))

for i, class_id in enumerate(class_ids):
    # Set colors on the bars
    colors = [color_dict.get(evaluation_type, 'skyblue') for evaluation_type in class_result[class_id]['_id']]
    axs[i].barh(class_result[class_id]['_id'], class_result[class_id]['avg_score'], color=colors)
    axs[i].set_title(f'Class ID {class_id}')
    axs[i].invert_yaxis()

plt.tight_layout()
plt.savefig('averageScoresClass.png')  # Save the plot as PNG
plt.show()
