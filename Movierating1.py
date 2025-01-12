import pandas as pd

# Load the dataset
df = pd.read_csv('path_to_your_downloaded_imdb_india_movies.csv')

# Display the first few rows of the dataset
df.head()

# Check for missing values
df.isnull().sum()

# Drop columns that are not useful for prediction (if any)
df.drop(['Column1', 'Column2'], axis=1, inplace=True)  # Replace 'Column1' and 'Column2' with actual names

# Drop duplicate rows (if any)
df.drop_duplicates(inplace=True)

# Handle missing values (you can drop or fill them)
df = df.dropna()  

import matplotlib.pyplot as plt
import seaborn as sns

# Distribution of movie ratings
plt.figure(figsize=(10, 6))
sns.histplot(df['Rating'], bins=20, kde=True)
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Check correlation between features
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
