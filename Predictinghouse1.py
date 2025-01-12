import pandas as pd

# Load the dataset
df = pd.read_csv('path_to_your_boston_housing.csv')

# Display the first few rows
df.head()

# Check the structure and data types
df.info()

# Display basic statistics
df.describe()

# Check for missing values
print(df.isnull().sum())

import seaborn as sns
import matplotlib.pyplot as plt

# Plot the correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

