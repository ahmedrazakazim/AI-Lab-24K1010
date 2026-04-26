import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder

data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)

encoder = LabelEncoder()
df['type_encoded'] = encoder.fit_transform(df['vehicle_type'])

X = df[['vehicle_serial_no', 'mileage', 'fuel_efficiency', 'maintenance_cost', 'type_encoded']]

km_unscaled = KMeans(n_clusters=3, random_state=42, n_init=10)
df['unscaled_cluster'] = km_unscaled.fit_predict(X)

scaler = StandardScaler()
numeric_features = ['vehicle_serial_no', 'mileage', 'fuel_efficiency', 'maintenance_cost']
X_scaled = X.copy()
X_scaled[numeric_features] = scaler.fit_transform(X[numeric_features])

km_scaled = KMeans(n_clusters=3, random_state=42, n_init=10)
df['scaled_cluster'] = km_scaled.fit_predict(X_scaled)

print("Vehicle clustering comparison using provided sample data")
print("\nAssignments without scaling:")
print(df[['vehicle_type', 'mileage', 'unscaled_cluster']])

print("\nAssignments with scaling:")
print(df[['vehicle_type', 'mileage', 'scaled_cluster']])

print("\nObservations:")
print("In the unscaled version, mileage completely dictates the clusters because the numbers are so large.")
print("Once scaled, fuel efficiency and maintenance costs actually influence the grouping results.")
