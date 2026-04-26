import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "venky73/spam-mails-dataset",
  "spam_ham_dataset.csv",
)

df.drop(columns=['Unnamed: 0', 'label'], inplace=True)
df.dropna(inplace=True)

print(f"Data loading successful. Total emails in dataset: {len(df)}")

x_train_raw, x_test_raw, y_train, y_test = train_test_split(
    df['text'], 
    df['label_num'], 
    test_size=0.2, 
    random_state=42
)

vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)

x_train = vectorizer.fit_transform(x_train_raw)
x_test = vectorizer.transform(x_test_raw)

print("Text data converted to numerical features.")

nb_classifier = MultinomialNB()
nb_classifier.fit(x_train, y_train)

print("Model training complete.")

y_pred = nb_classifier.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print("\n--- Evaluation Results ---")
print(f"Model Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
plt.title("Confusion Matrix")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.show()

def check_new_email(text):
    vectorized_input = vectorizer.transform([text])
    prediction = nb_classifier.predict(vectorized_input)[0]
    return "SPAM" if prediction == 1 else "NOT SPAM"

incoming_messages = [
    "You have won a $500 gift card! Click here to claim your reward immediately.",
    "Hey, just checking in to see if you're coming to the dinner tonight?",
    "Your package is waiting for delivery. Please update your shipping address."
]

print("\n--- Testing New Emails ---")
for msg in incoming_messages:
    label = check_new_email(msg)
    print(f"Label: {label} | Text: {msg[:50]}...")
