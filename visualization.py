import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("titanic.csv")

# ------------------------
# Survival Count Graph
# ------------------------

plt.figure(figsize=(6,4))

df['Survived'].value_counts().plot(kind='bar')

plt.title("Survival Count")
plt.xlabel("Survived (0=No, 1=Yes)")
plt.ylabel("Number of Passengers")

plt.savefig("survival_count.png")

plt.show()


# ------------------------
# Male vs Female Survival
# ------------------------

plt.figure(figsize=(6,4))

sns.countplot(x='Sex', hue='Survived', data=df)

plt.title("Male vs Female Survival")

plt.savefig("male_female_survival.png")

plt.show()


# ------------------------
# Age Distribution
# ------------------------

plt.figure(figsize=(8,5))

plt.hist(df['Age'].dropna(), bins=20)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

plt.savefig("age_distribution.png")

plt.show()


# ------------------------
# Correlation Heatmap
# ------------------------

plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include=['number'])

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.savefig("correlation_heatmap.png")

plt.show()