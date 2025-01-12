from sklearn.model_selection import GridSearchCV

# Hyperparameter tuning for RandomForestRegressor
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(estimator=RandomForestRegressor(random_state=42), param_grid=param_grid, cv=3, n_jobs=-1)
grid_search.fit(X_train, y_train)

# Best parameters from GridSearchCV
print(f'Best parameters: {grid_search.best_params_}')

# Predict with the best model
best_rf_model = grid_search.best_estimator_
y_pred_best = best_rf_model.predict(X_test)

# Evaluate the tuned model
print(f'Mean Absolute Error: {mean_absolute_error(y_test, y_pred_best)}')
print(f'Mean Squared Error: {mean_squared_error(y_test, y_pred_best)}')
print(f'R-squared: {r2_score(y_test, y_pred_best)}')
