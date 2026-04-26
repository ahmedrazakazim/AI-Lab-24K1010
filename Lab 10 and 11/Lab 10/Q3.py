import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

np.random.seed(42)
customer_count = 500

df = pd.DataFrame({
    'total_spending': np.random.exponential(500, customer_count),
    'age': np.random.randint(18, 70, customer_count),
    'num_visits': np.random.randint(1, 30, customer_count),
    'purchase_freq': np.random.randint(1, 20, customer_count),
})

df.loc[np.random.choice(customer_count, 10), 'age'] = np.nan
df.loc[np.random.choice(customer_count, 5), 'total_spending'] = np.nan

df['age'] = df['age'].fillna(df['age'].median())
df['total_spending'] = df['total_spending'].fillna(df['total_spending'].median())

q1 = df['total_spending'].quantile(0.25)
q3 = df['total_spending'].quantile(0.75)
iqr = q3 - q1
upper_bound = q3 + 1.5 * iqr
df['total_spending'] = df['total_spending'].clip(upper=upper_bound)

df['label'] = ((df['total_spending'] > 500) | (df['num_visits'] > 15)).astype(int)

X = df.drop('label', axis=1)
y = df['label']

print(f"Data Cleaning Complete. Dataset contains {len(df)} customer records.")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

svm_model = SVC(kernel='linear', C=1.0)
svm_model.fit(X_train_scaled, y_train)

print("\n--- Model 1: Support Vector Machine (Separating Hyperplane) ---")
y_pred_svm = svm_model.predict(X_test_scaled)
print(f"SVM Accuracy: {accuracy_score(y_test, y_pred_svm):.4f}")
print(classification_report(y_test, y_pred_svm))

tree_model = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_model.fit(X_train, y_train)

print("\n--- Model 2: Decision Tree (Classification Rules) ---")
tree_rules = export_text(tree_model, feature_names=list(X.columns))
print("Generated Logic Rules:")
print(tree_rules)

y_pred_tree = tree_model.predict(X_test)
print(f"Decision Tree Accuracy: {accuracy_score(y_test, y_pred_tree):.4f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ConfusionMatrixDisplay.from_predictions(y_test, y_pred_svm, display_labels=['Low-Value', 'High-Value'], cmap='Blues', ax=ax1)
ax1.set_title("SVM Confusion Matrix")

ConfusionMatrixDisplay.from_predictions(y_test, y_pred_tree, display_labels=['Low-Value', 'High-Value'], cmap='Reds', ax=ax2)
ax2.set_title("Decision Tree Confusion Matrix")

plt.tight_layout()
plt.show()

new_prospect = pd.DataFrame([{
    'total_spending': 850.0,
    'age': 42,
    'num_visits': 22,
    'purchase_freq': 15
}])

prospect_scaled = scaler.transform(new_prospect)
svm_result = svm_model.predict(prospect_scaled)[0]
tree_result = tree_model.predict(new_prospect)[0]

print("\n--- Real-Time Prediction for New Customer ---")
print(f"Customer Data: Spending=$850, Visits=22")
print(f"SVM Classification: {'High-Value' if svm_result == 1 else 'Low-Value'}")
print(f"Decision Tree Classification: {'High-Value' if tree_result == 1 else 'Low-Value'}")
