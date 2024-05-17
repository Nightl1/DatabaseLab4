import matplotlib.pyplot as plt
import pandas as pd

# Read the csv doc
df = pd.read_csv('sample_guides.planets.csv')

# sort by the order from sun
df_sorted = df.sort_values(by='orderFromSun')

# replace id with order
df_sorted['_id'] = df_sorted['orderFromSun']

# print(df_sorted)


# colors for each atmosphere type
colors = {'CO2': '#00CED1', 'N': '#00FFFF', 'O2': '#228B22', 'Ar': '#00FA9A', 'H2': '#008080', 'He': '#191970', 'CH4': '#00FF00'}

# Plotting
plt.figure(figsize=(10, 6))
for index, row in df_sorted.iterrows():
    atmosphere = row['mainAtmosphere[0]']
    color = colors.get(atmosphere, 'gray')  # Default to gray if atmosphere is missing or not in the dictionary
    plt.plot([index, index], [row['surfaceTemperatureC.min'], row['surfaceTemperatureC.max']], color=color, marker='o', label=row['name'])

# Customizing the plot
plt.xlabel('Planet')
plt.ylabel('Surface Temperature (°C)')
plt.title('Surface Temperature of Planets')
plt.xticks(range(len(df_sorted)), df_sorted['name'], rotation=45)
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()