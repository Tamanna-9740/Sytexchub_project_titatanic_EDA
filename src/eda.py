import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('titanic')

# Data inspection
print(df.info())
print(df.isnull().sum())

# Survival analysis
print(df.groupby('sex')['survived'].mean())
print(df.groupby('class')['survived'].mean())

# Age groups
df['age_group'] = pd.cut(df['age'],
                        bins=[0,12,18,35,60,100],
                        labels=['Child','Teen','Young Adult','Adult','Senior'])

print(df.groupby('age_group')['survived'].mean())

# Visualization
sns.barplot(x='sex', y='survived', data=df)
plt.savefig('images/survival_by_sex.png')
plt.clf()

sns.barplot(x='class', y='survived', data=df)
plt.savefig('images/survival_by_class.png')
plt.clf()

sns.boxplot(x='survived', y='age', data=df)
plt.savefig('images/age_distribution.png')
plt.clf()