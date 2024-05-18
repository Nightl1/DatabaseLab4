import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt

# Connect to the database
client = MongoClient('mongodb://localhost:27017/')
db = client['DatabaseLab4']
planets_collection = db['Planets']

# list of planets to make a pie graph for
target_planets = ['Venus', 'Earth', 'Mars', 'Saturn', 'Jupiter', 'Neptune']

# colors for each atmosphere
colors = {
    'CO2': '#00CED1',
    'N': '#00FFFF',
    'Ar': '#00FA9A',
    'O2': '#228B22',
    'H2': '#008080',
    'He': '#191970',
    'CH4': '#00FF00'
}

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle("Main Composition of Planets' Atmosphere in Solar System", fontweight='bold')

for i, planet in enumerate(target_planets):
    planet_data = list(planets_collection.find({'name': planet}))
    planet_data = planet_data[0]  
    
    main_atmosphere = planet_data['mainAtmosphere']
    
    
    atmosphere_counts = {atmosphere: main_atmosphere.count(atmosphere) for atmosphere in set(main_atmosphere)}
    
    # Create a pie chart plaets
    ax = axes[i // 3, i % 3]
    ax.set_title(planet)
    ax.pie(atmosphere_counts.values(), labels=atmosphere_counts.keys(), colors=[colors.get(atmosphere) for atmosphere in atmosphere_counts.keys()])

plt.tight_layout()
plt.savefig('mainCompositionofPlantsAtmosphereinSolorSystem.png')  # Save the imgage as PNG
plt.show()
