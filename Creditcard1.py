import pandas as pd

# Load the dataset
df = pd.read_csv('path_to_your_downloaded_creditcardfraud.csv')

# Display the first few rows of the dataset
df.head()

# Check for missing values
df.isnull().sum()

# Drop missing values if any
df.dropna(inplace=True)

from sklearn.preprocessing import StandardScaler

# Scaling the features (excluding the target variable 'Class')
scaler = StandardScaler()
df_scaled = df.copy()

# Standardizing all features except 'Class' (target variable)
df_scaled[df.columns[:-1]] = scaler.fit_transform(df[df.columns[:-1]])

# Check the scaled dataset
df_scaled.head()

