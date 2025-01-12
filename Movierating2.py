# Convert categorical columns into numerical values (e.g., Genre, Language)
df['Genre'] = df['Genre'].astype('category').cat.codes  # Example: Convert genre to a numerical value
df['Language'] = df['Language'].astype('category').cat.codes  # Example: Convert language to a numerical value

# Extract year from the 'Release Date' column (if applicable)
df['Release_Year'] = pd.to_datetime(df['Release Date'], errors='coerce').dt.year

# Drop any remaining irrelevant columns
df.drop(['Release Date'], axis=1, inplace=True)

from sklearn.model_selection import train_test_split

# Define features and target
X = df.drop('Rating', axis=1)  # Drop the target variable 'Rating'
y = df['Rating']  # The target variable is the 'Rating'

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Initialize and train the Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
print(f'Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}')
print(f'Mean Squared Error: {mean_squared_error(y_test, y_pred)}')
print(f'R-squared: {r2_score(y_test, y_pred)}')
