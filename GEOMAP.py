#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd
import matplotlib.pyplot as plt

# List of countries that accept water fluoridation
fluoridation_countries = [
    'Ethiopia', 'Nigeria', 'South Africa', 'Kenya', 'Egypt',
    'Malaysia', 'Pakistan', 'India', 'China', 'Sri Lanka', 'Japan',
    'United States of America',
    'Ireland', 'Norway', 'Scotland', 'Switzerland', 'Netherlands', 'Luxembourg',
    'Israel', 'France', 'Germany', 'Hungary', 'Czech Republic', 'Austria', 'Belgium'
]

# Load world map data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filter the countries that accept water fluoridation
fluoridation_map = world[world['name'].isin(fluoridation_countries)]

# Plot the map
fig, ax = plt.subplots(figsize=(15, 10))
world.plot(ax=ax, color='lightgray', edgecolor='black')
fluoridation_map.plot(ax=ax, color='blue', edgecolor='black', label='Fluoridation Countries')

# Add country labels
for x, y, label in zip(fluoridation_map.geometry.centroid.x, fluoridation_map.geometry.centroid.y, fluoridation_map['name']):
    ax.text(x, y, label, fontsize=8, ha='center', va='center', color='white')

# Set plot title and legend
ax.set_title('Countries Accepting Water Fluoridation', fontsize=16)
ax.legend()

# Show the map
plt.show()


# In[ ]:




