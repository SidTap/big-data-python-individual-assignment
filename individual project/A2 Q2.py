#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
from itertools import combinations

# Take the input string of Cartesian coordinates from the user
coords_list = [[0,0],[0,1],[1,1],[1,0],[2,1],[2,0],[3,1],[3,0],[1,0],[0,1],[1,2],[2,1]]
coords_list = [list(t) for t in set(tuple(element) for element in coords_list)]

# Find all unique combinations of four points from the list that form a rectangle
rectangles = []
for combo in combinations(coords_list, 4):
    # Check if the four points form a rectangle
    x_coords = [point[0] for point in combo]
    y_coords = [point[1] for point in combo]
    if len(set(x_coords)) == 2 and len(set(y_coords)) == 2:
        rectangles.append(combo)

# Create a pandas DataFrame from the list of quadrilaterals
df = pd.DataFrame(rectangles, columns=['point1', 'point2', 'point3', 'point4'])

# Function to calculate the distance between two points
def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# Calculate the distance between opposite sides of each rectangle
df['dist1'] = df.apply(lambda row: distance(row['point1'], row['point3']), axis=1)
df['dist2'] = df.apply(lambda row: distance(row['point2'], row['point4']), axis=1)

# Check if each rectangle is a square
df['isSquare'] = df.apply(lambda row: 'yes' if row['dist1'] == row['dist2'] else 'no', axis=1)

# Calculate the slopes of opposite sides of each square
df['slope1'] = df.apply(lambda row: (row['point3'][1] - row['point1'][1]) / (row['point3'][0] - row['point1'][0]) if row['point3'][0] != row['point1'][0] else float('inf'), axis=1)
df['slope2'] = df.apply(lambda row: (row['point4'][1] - row['point2'][1]) / (row['point4'][0] - row['point2'][0]) if row['point4'][0] != row['point2'][0] else float('inf'), axis=1)

# Check if each square's sides are parallel to the x-axis
df['isParallel'] = df.apply(lambda row: 'yes' if row['slope1'] == 0 and row['slope2'] == 0 or row['slope1'] == float('inf') and row['slope2'] == float('inf') else None, axis=1)

len(df_result)

# output is 3
# Time complexity:O(n^4) because the combination are created
# Space complexity:O(n^4) because it stores the combinations


# In[ ]:





# In[ ]:





# In[ ]:




