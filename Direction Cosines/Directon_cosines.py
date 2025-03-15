import numpy as np
import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt

# Function to calculate direction cosines
def direction_cosines(x, y, z):
    magnitude = np.sqrt(x**2 + y**2 + z**2)
    l = x / magnitude
    m = y / magnitude
    n = z / magnitude
    return l, m, n

# Example coordinates of a line in 3D space
x, y, z = 3, 4, 5

# Calculate direction cosines
l, m, n = direction_cosines(x, y, z)

# Create a DataFrame for seaborn
data = pd.DataFrame({
    'Direction Cosines': ['l', 'm', 'n'],
    'Values': [l, m, n]
})

# Plot using seaborn
sns.barplot(x='Direction Cosines', y='Values', data=data)
plt.title('Direction Cosines of a Line in 3D Space')
plt.show()