import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris_data = pd.read_csv(url, names=column_names)

# Display the first few rows of the dataset
print("First few rows of the Iris dataset:")
print(iris_data.head())

# Summary statistics of the dataset
print("\nSummary statistics of the Iris dataset:")
print(iris_data.describe())

# Visualize the distribution of classes
plt.figure(figsize=(8, 6))
iris_data['class'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Iris Classes')
plt.xlabel('Class')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Split the dataset into features (X) and target variable (y)
X = iris_data.drop('class', axis=1)
y = iris_data['class']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
clf.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy of the Random Forest classifier:", accuracy)

# Display classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
