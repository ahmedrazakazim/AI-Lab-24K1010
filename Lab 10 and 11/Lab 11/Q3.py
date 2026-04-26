import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import kagglehub
from kagglehub import KaggleDatasetAdapter
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

exam_records = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "spscientist/students-performance-in-exams",
    "StudentsPerformance.csv"
)

exam_records['GPA'] = (exam_records[['math score', 'reading score', 'writing score']].mean(axis=1) / 100) * 4.0
np.random.seed(42)
exam_records['study_hours'] = np.random.randint(5, 40, len(exam_records))
exam_records['attendance_rate'] = np.random.randint(60, 100, len(exam_records))
exam_records['student_id'] = [f"24K-{3000 + i}" for i in range(len(exam_records))]

input_features = ['GPA', 'study_hours', 'attendance_rate']
X_processed = StandardScaler().fit_transform(exam_records[input_features])

distortion = []
for k in range(2, 7):
    k_model = KMeans(n_clusters=k, random_state=42, n_init=10)
    k_model.fit(X_processed)
    distortion.append(k_model.inertia_)

plt.figure(figsize=(6, 4))
plt.plot(range(2, 7), distortion, marker='x', color='blue')
plt.title('Optimal Cluster Identification')
plt.xlabel('Number of Groups')
plt.ylabel('Inertia Score')
plt.show()

final_k_choice = 3
exam_records['Academic_Cluster'] = KMeans(n_clusters=final_k_choice, random_state=42, n_init=10).fit_predict(X_processed)

plt.figure(figsize=(10, 6))
plt.scatter(exam_records['study_hours'], exam_records['GPA'], c=exam_records['Academic_Cluster'], cmap='coolwarm', alpha=0.6)
plt.title('FAST NUCES Karachi Student Segmentation')
plt.xlabel('Weekly Study Hours')
plt.ylabel('GPA')
plt.show()

print("Final Student Record Segmentations")
print(exam_records[['student_id', 'GPA', 'study_hours', 'attendance_rate', 'Academic_Cluster']].head(15))
