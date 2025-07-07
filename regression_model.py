from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('bread_delivery_data.csv')

# One-hot encode categorical variables (turns categories into columns of 0/1s)
df_encoded = pd.get_dummies(df, columns=['delivery_time', 'weather', 'traffic_level'], drop_first=True)

# axis=1 for column, 0 for row
X = df_encoded.drop('delivery_cost', axis=1)
y = df_encoded['delivery_cost']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = LinearRegression()

# Train (fit) the model on training data
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error: {mae:.2f}')
print(f'Root Mean Squared Error: {rmse:.2f}')
print(f'R^2 Score: {r2:.3f}')

coeffs = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
}).sort_values(by='Coefficient', key=abs, ascending=False)

print('\nFeature Importance (Absolute Value):')
print(coeffs)

plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel('Actual Delivery Cost')
plt.ylabel('Predicted Delivery Cost')
plt.title('Actual vs Predicted Delivery Cost')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red')
plt.show()

