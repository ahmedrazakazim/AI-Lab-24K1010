import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
from kagglehub import KaggleDatasetAdapter
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "camnugent/california-housing-prices",
    "housing.csv"
)

for col in df.columns:
    if df[col].dtype in [np.float64, np.int64]:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

print("Data loading and cleaning finished.")

df = pd.get_dummies(df, columns=['ocean_proximity'], drop_first=True)

target_col = "median_house_value"
features_x = df.drop(target_col, axis=1)
target_y = df[target_col]

print("\nFeatures used for training:")
print(list(features_x.columns))

x_train, x_test, y_train, y_test = train_test_split(
    features_x, target_y, test_size=0.2, random_state=42
)

print("\nDataset split into training and testing partitions.")

housing_model = RandomForestRegressor(n_estimators=100, random_state=42)
housing_model.fit(x_train, y_train)

print("Random Forest model training complete.")

predictions = housing_model.predict(x_test)

mae_val = mean_absolute_error(y_test, predictions)
mse_val = mean_squared_error(y_test, predictions)
r2_val = r2_score(y_test, predictions)

print("\n--- Model Performance Evaluation ---")
print(f"Mean Absolute Error: ${mae_val:,.2f}")
print(f"Mean Squared Error: {mse_val:,.2f}")
print(f"R2 Score: {r2_val:.4f}")

feature_importance_scores = housing_model.feature_importances_
feature_names = features_x.columns

plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importance_scores, y=feature_names, hue=feature_names, palette='viridis', legend=False)
plt.title("Key Drivers of Housing Prices")
plt.xlabel("Importance Level")
plt.ylabel("Feature Name")
plt.tight_layout()
plt.show()

new_property_data = pd.DataFrame([{
    'longitude': -122.23,
    'latitude': 37.88,
    'housing_median_age': 41.0,
    'total_rooms': 880.0,
    'total_bedrooms': 129.0,
    'population': 322.0,
    'households': 126.0,
    'median_income': 8.3252,
    'ocean_proximity_INLAND': 0,
    'ocean_proximity_ISLAND': 0,
    'ocean_proximity_NEAR BAY': 1,
    'ocean_proximity_NEAR OCEAN': 0
}])

for col in features_x.columns:
    if col not in new_property_data.columns:
        new_property_data[col] = 0

new_property_data = new_property_data[features_x.columns]

estimated_value = housing_model.predict(new_property_data)
print(f"\nEstimated Market Value for the New Property: ${estimated_value[0]:,.2f}")
