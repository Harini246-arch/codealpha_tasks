import pandas as pd

# Read Titanic Dataset
df = pd.read_csv("titanic.csv")

# First 5 rows
print("========== FIRST 5 ROWS ==========")
print(df.head())

# Dataset Shape
print("\n========== DATASET SHAPE ==========")
print(df.shape)

# Dataset Information
print("\n========== DATASET INFO ==========")
print(df.info())

# Missing Values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Statistics
print("\n========== STATISTICS ==========")
print(df.describe())
import matplotlib.pyplot as plt

# Survival Count Plot
df['Survived'].value_counts().plot(kind='bar')

plt.title("Survival Count")
plt.xlabel("Survived (0=No, 1=Yes)")
plt.ylabel("Number of Passengers")

plt.show()
import seaborn as sns

plt.figure(figsize=(6,4))

sns.countplot(x='Sex', hue='Survived', data=df)

plt.title("Male vs Female Survival")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.show()
plt.figure(figsize=(8,5))

plt.hist(df['Age'].dropna(), bins=20)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

plt.show()
# Correlation Heatmap

plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include=['number'])

sns.heatmap(numeric_df.corr(),
            annot=True,
            cmap='coolwarm')

plt.title("Correlation Heatmap")

plt.show()