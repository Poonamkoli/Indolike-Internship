# Select relevant columns for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Check the selected features
X.head()

from sklearn.preprocessing import StandardScaler

# Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
