import pandas as pd

# Read the csv doc
df = pd.read_csv('sample_guides.planets.csv')

# Sort by orderFromSun and then name
df_sorted = df.sort_values(by=['orderFromSun', 'name'])

# Replace _id with orderFromSun
df_sorted['_id'] = df_sorted['orderFromSun']

df_melted = df_sorted.melt(id_vars=['orderFromSun', 'name'], value_vars=['mainAtmosphere[0]', 'mainAtmosphere[1]', 'mainAtmosphere[2]'], value_name='mainAtmosphere')

df_melted.drop(columns=['variable'], inplace=True)

df_melted = df_melted[df_melted['mainAtmosphere'].notna()]

# Match mainAtmosphere to a color
def map_color(mainAtmosphere):
    if mainAtmosphere == 'CO2':
        return '#00CED1'
    elif mainAtmosphere == 'N':
        return '#00FFFF'
    elif mainAtmosphere == 'O2':
        return '#228B22'
    elif mainAtmosphere == 'Ar':
        return '#00FA9A'
    elif mainAtmosphere == 'H2':
        return '#008080'
    elif mainAtmosphere == 'He':
        return '#191970'
    elif mainAtmosphere == 'CH4':
        return '#00FF00'
    else:
        return None

# create color_values column
df_melted['color_values'] = df_melted['mainAtmosphere'].apply(map_color)
result_df = df_melted[['orderFromSun', 'name', 'mainAtmosphere', 'color_values']]
print(result_df)
