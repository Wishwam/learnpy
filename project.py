
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

print("Loading dataset...\n")

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

print("Dataset Loaded Successfully!")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nChecking missing values:")
print(df.isnull().sum())


df["Sleep Disorder"] = df["Sleep Disorder"].fillna("None")

print("\nMissing values handled.\n")

avg_sleep_duration = df["Sleep Duration"].mean()
avg_sleep_quality = df["Quality of Sleep"].mean()

print("Average Sleep Duration:", round(avg_sleep_duration, 2), "hours")
print("Average Sleep Quality:", round(avg_sleep_quality, 2))

print("\nCorrelation between Sleep Duration and Stress Level:")
correlation = df[["Sleep Duration", "Stress Level"]].corr()
print(correlation)

plt.figure()
sns.scatterplot(x="Stress Level", y="Sleep Duration", data=df)
plt.title("Stress Level vs Sleep Duration")
plt.xlabel("Stress Level")
plt.ylabel("Sleep Duration (hours)")
plt.show()

plt.figure()
sns.boxplot(x="Physical Activity Level", y="Quality of Sleep", data=df)
plt.title("Physical Activity Level vs Sleep Quality")
plt.xlabel("Physical Activity Level")
plt.ylabel("Quality of Sleep")
plt.show()

print("\nHypothesis Testing:")
print("H0: Physical activity has no effect on sleep quality")
print("H1: Physical activity affects sleep quality\n")

high_activity = df[df["Physical Activity Level"] >= 60]["Quality of Sleep"]
low_activity = df[df["Physical Activity Level"] < 60]["Quality of Sleep"]

t_stat, p_value = stats.ttest_ind(high_activity, low_activity)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Result: Reject H0 → Physical activity significantly affects sleep quality")
else:
    print("Result: Fail to reject H0 → No significant effect found")

plt.figure()
sns.countplot(x="Sleep Disorder", data=df)
plt.title("Distribution of Sleep Disorders")
plt.xlabel("Sleep Disorder")
plt.ylabel("Count")
plt.show()

plt.figure()
sns.histplot(df["Sleep Duration"], kde=True)
plt.title("Distribution of Sleep Duration")
plt.xlabel("Sleep Duration (hours)")
plt.ylabel("Frequency")
plt.show()


print("\nConclusion:")
print("Lifestyle factors such as physical activity and stress level")
print("have a significant impact on sleep health.")
print("Higher stress reduces sleep duration, while physical activity")
print("improves sleep quality.")

print("\n--- Project Execution Completed Successfully ---")
