# Residual plot
sns.residplot(x=y_test, y=y_pred, lowess=True, color='blue')
plt.title('Residual Plot')
plt.xlabel('Actual Values')
plt.ylabel('Residuals')
plt.show()

# Plot feature importances
import numpy as np

importances = rf_model.feature_importances_
indices = np.argsort(importances)[::-1]
features = X.columns

plt.figure(figsize=(10, 6))
plt.title("Feature Importances")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), features[indices], rotation=90)
plt.show()

import joblib

# Save the model
joblib.dump(rf_model, 'housing_price_model.pkl')

# Load the model
loaded_model = joblib.load('housing_price_model.pkl')
