import matplotlib.pyplot as plt
import seaborn as sns

# Class distribution (fraud vs. non-fraud)
sns.countplot(x='Class', data=df)
plt.title('Distribution of Fraudulent and Non-Fraudulent Transactions')
plt.show()

# Percentage of fraud and non-fraud transactions
fraud_percentage = df['Class'].value_counts(normalize=True) * 100
print(fraud_percentage)

plt.figure(figsize=(12, 8))
sns.heatmap(df_scaled.corr(), annot=False, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# Define the features and the target
X = df_scaled.drop('Class', axis=1)  # Features (excluding target variable)
y = df_scaled['Class']  # Target variable ('Class' indicates fraud)

