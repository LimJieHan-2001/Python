import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(data_url)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Summary statistics of the dataset
print("\nSummary statistics of the dataset:")
print(df.describe())

# Histogram of sepal length
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='sepal_length', bins=20, kde=True)
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# Box plot of petal width for each species
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='species', y='petal_width')
plt.title('Box plot of Petal Width by Species')
plt.xlabel('Species')
plt.ylabel('Petal Width')
plt.show()

# Scatter plot of sepal length vs sepal width colored by species
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species')
plt.title('Scatter Plot of Sepal Length vs Sepal Width (Colored by Species)')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend(title='Species')
plt.show()
