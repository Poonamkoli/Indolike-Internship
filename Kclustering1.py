import pandas as pd

# Load the dataset
df = pd.read_csv('path_to_your_downloaded_dataset.csv')

# Display the first few rows
df.head()

# Check for missing values
df.isnull().sum()

# Drop unnecessary columns (if any)
df.drop(['CustomerID'], axis=1, inplace=True)

# Check data types and convert if necessary
df['Age'] = df['Age'].astype(float)

# Handle missing values if any (drop or fill)
df = df.dropna()  # You can also use df.fillna() to fill missing values
