#!/usr/bin/env python
# coding: utf-8

# In[2]:


import geopandas as gpd
import matplotlib.pyplot as plt

# List of countries
fluoridation_countries = [
    'Ethiopia', 'Nigeria', 'South Africa', 'Kenya', 'Egypt',
    'Malaysia', 'Pakistan', 'India', 'China', 'Sri Lanka', 'Japan',
    'United States of America',
    'Ireland', 'Norway', 'Scotland', 'Switzerland', 'Netherlands', 'Luxembourg',
    'Israel', 'France', 'Germany', 'Hungary', 'Czech Republic', 'Austria', 'Belgium'
]

non_fluoridation_countries = [
    'Denmark', 'Finland', 'Greece', 'Iceland', 'Italy', 'Northern Ireland'
]

# Load world map data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filter the countries that accept and reject water fluoridation
fluoridation_map = world[world['name'].isin(fluoridation_countries)]
non_fluoridation_map = world[world['name'].isin(non_fluoridation_countries)]

# Plot the map
fig, ax = plt.subplots(figsize=(15, 10))
world.plot(ax=ax, color='lightgray', edgecolor='black')
fluoridation_map.plot(ax=ax, color='blue', edgecolor='black', label='Fluoridation Countries')
non_fluoridation_map.plot(ax=ax, color='red', edgecolor='black', label='Non-Fluoridation Countries')

# Add country labels
for x, y, label in zip(fluoridation_map.geometry.centroid.x, fluoridation_map.geometry.centroid.y, fluoridation_map['name']):
    ax.text(x, y, label, fontsize=8, ha='center', va='center', color='white')

for x, y, label in zip(non_fluoridation_map.geometry.centroid.x, non_fluoridation_map.geometry.centroid.y, non_fluoridation_map['name']):
    ax.text(x, y, label, fontsize=8, ha='center', va='center', color='white')

# Set plot title and legend
ax.set_title('Water Fluoridation Status by Country', fontsize=16)
ax.legend(title='Fluoridation Status', loc='upper left')

# Show the map
plt.show()


# In[3]:


import geopandas as gpd
import matplotlib.pyplot as plt

# List of countries
fluoridation_countries = [
    'Ethiopia', 'Nigeria', 'South Africa', 'Kenya', 'Egypt',
    'Malaysia', 'Pakistan', 'India', 'China', 'Sri Lanka', 'Japan',
    'United States of America',
    'Ireland', 'Norway', 'Scotland', 'Switzerland', 'Netherlands', 'Luxembourg',
    'Israel', 'France', 'Germany', 'Hungary', 'Czech Republic', 'Austria', 'Belgium'
]

non_fluoridation_countries = [
    'Denmark', 'Finland', 'Greece', 'Iceland', 'Italy', 'Northern Ireland'
]

# Load world map data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filter the countries that accept and reject water fluoridation
fluoridation_map = world[world['name'].isin(fluoridation_countries)]
non_fluoridation_map = world[world['name'].isin(non_fluoridation_countries)]

# Plot the map
fig, ax = plt.subplots(figsize=(15, 10))
world.plot(ax=ax, color='lightgray', edgecolor='black')
fluoridation_map.plot(ax=ax, color='blue', edgecolor='black', label='Accepts Fluoridation')
non_fluoridation_map.plot(ax=ax, color='red', edgecolor='black', label='Rejects Fluoridation')

# Add country labels
for x, y, label in zip(fluoridation_map.geometry.centroid.x, fluoridation_map.geometry.centroid.y, fluoridation_map['name']):
    ax.text(x, y, label, fontsize=8, ha='center', va='center', color='white')

for x, y, label in zip(non_fluoridation_map.geometry.centroid.x, non_fluoridation_map.geometry.centroid.y, non_fluoridation_map['name']):
    ax.text(x, y, label, fontsize=8, ha='center', va='center', color='white')

# Set plot title and legend
ax.set_title('Water Fluoridation Status by Country', fontsize=16)
ax.legend(title='Fluoridation Status', loc='upper left')

# Show the map
plt.show()


# In[4]:


import geopandas as gpd
import matplotlib.pyplot as plt

# List of countries
fluoridation_countries = [
    'Ethiopia', 'Nigeria', 'South Africa', 'Kenya', 'Egypt',
    'Malaysia', 'Pakistan', 'India', 'China', 'Sri Lanka', 'Japan',
    'United States of America',
    'Ireland', 'Norway', 'Scotland', 'Switzerland', 'Netherlands', 'Luxembourg',
    'Israel', 'France', 'Germany', 'Hungary', 'Czech Republic', 'Austria', 'Belgium'
]

non_fluoridation_countries = [
    'Denmark', 'Finland', 'Greece', 'Iceland', 'Italy', 'Northern Ireland'
]

# Load world map data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Create a new column to indicate fluoridation status
world['Fluoridation'] = world['name'].apply(lambda x: 'Accepts' if x in fluoridation_countries else ('Rejects' if x in non_fluoridation_countries else 'Unknown'))

# Plot the map
fig, ax = plt.subplots(figsize=(15, 10))
world[world['Fluoridation'] == 'Accepts'].plot(ax=ax, color='blue', edgecolor='black', label='Accepts Fluoridation')
world[world['Fluoridation'] == 'Rejects'].plot(ax=ax, color='red', edgecolor='black', label='Rejects Fluoridation')
world[world['Fluoridation'] == 'Unknown'].plot(ax=ax, color='lightgray', edgecolor='black', label='Unknown')

# Add country labels
for x, y, label in zip(world[world['Fluoridation'] == 'Accepts'].geometry.centroid.x, world[world['Fluoridation'] == 'Accepts'].geometry.centroid.y, world[world['Fluoridation'] == 'Accepts']['name']):
    ax.text(x, y, label, fontsize=8, ha='center', va='center', color='white')

for x, y, label in zip(world[world['Fluoridation'] == 'Rejects'].geometry.centroid.x, world[world['Fluoridation'] == 'Rejects'].geometry.centroid.y, world[world['Fluoridation'] == 'Rejects']['name']):
    ax.text(x, y, label, fontsize=8, ha='center', va='center', color='white')

# Set plot title and legend
ax.set_title('Water Fluoridation Status by Country', fontsize=16)
ax.legend(title='Fluoridation Status', loc='upper left')

# Show the map
plt.show()


# In[ ]:




