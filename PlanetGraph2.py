import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df1 = pd.read_csv('sample_guides.planets.csv')

# Sort by sun then name
df1_sorted = df1.sort_values(by=['orderFromSun', 'name'])

# Replace _id with orderFromSun
df1_sorted['_id'] = df1_sorted['orderFromSun']


df1_melted = df1_sorted.melt(id_vars=['orderFromSun', 'name'], value_vars=['mainAtmosphere[0]', 'mainAtmosphere[1]', 'mainAtmosphere[2]'], value_name='mainAtmosphere')

df1_melted.drop(columns=['variable'], inplace=True)

df1_melted = df1_melted[df1_melted['mainAtmosphere'].notna()]

# Match mainAtmosphere to a color
def map_color(mainAtmosphere):
    colors = {
        'CO2': '#00CED1',
        'N': '#00FFFF',
        'Ar': '#00FA9A',
        'O2': '#228B22',
        'H2': '#008080',
        'He': '#191970',
        'CH4': '#00FF00'
    }
    return colors.get(mainAtmosphere)

# create color_values column 
df1_melted['color_values'] = df1_melted['mainAtmosphere'].apply(map_color)

# Read the second CSV file
df2 = pd.read_csv('sample_guides.planets.csv')

# Merge the two dataframes on 'name'
merged_df = pd.merge(df1_melted, df2, on='name')

# Create subplots for each planet
plt.figure(figsize=(15, 10))
plt.suptitle("Main Composition of Planets' Atmosphere in Solar System", fontweight='bold')

for i, planet in enumerate(['Venus', 'Earth', 'Mars', 'Saturn', 'Jupiter', 'Neptune'], start=1):
    plt.subplot(2, 3, i)
    plt.title(planet)
    
    planet_data = merged_df[merged_df['name'] == planet]
    
    atmosphere_counts = planet_data['mainAtmosphere'].value_counts()
    
    # Create pie chart
    plt.pie(atmosphere_counts, labels=atmosphere_counts.index, colors=[map_color(x) for x in atmosphere_counts.index])

plt.tight_layout()
plt.savefig('mainCompositionofPlantsAtmosphereinSolorSystem.png')  # Save the plot as PNG
plt.show()
