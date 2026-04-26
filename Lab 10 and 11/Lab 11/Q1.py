import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import kagglehub
from kagglehub import KaggleDatasetAdapter
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder

customer_data = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "vjchoudhary7/customer-segmentation-tutorial-in-python",
    "Mall_Customers.csv"
)

customer_data['Gender'] = LabelEncoder().fit_transform(customer_data['Gender'])
features = customer_data.drop(['CustomerID'], axis=1)

raw_model = KMeans(n_clusters=5, random_state=42, n_init=10)
customer_data['raw_labels'] = raw_model.fit_predict(features)

scaler = StandardScaler()
cols_to_transform = ['Gender', 'Annual Income (k$)', 'Spending Score (1-100)']
partially_scaled = features.copy()
partially_scaled[cols_to_transform] = scaler.fit_transform(features[cols_to_transform])

scaled_model = KMeans(n_clusters=5, random_state=42, n_init=10)
customer_data['scaled_labels'] = scaled_model.fit_predict(partially_scaled)

print("Customer Segmentation Overview")
print("Inertia without scaling:", raw_model.inertia_)
print("Inertia with partial scaling:", scaled_model.inertia_)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(features['Annual Income (k$)'], features['Spending Score (1-100)'], c=customer_data['raw_labels'], cmap='viridis')
plt.title("No Scaling Applied")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")

plt.subplot(1, 2, 2)
plt.scatter(features['Annual Income (k$)'], features['Spending Score (1-100)'], c=customer_data['scaled_labels'], cmap='magma')
plt.title("Scaling Excluding Age")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()

print("\nComparison results:")
print("The unscaled version is dominated by income and spending score ranges.")
print("The version with scaling shows different group boundaries as other features gain more weight.")
