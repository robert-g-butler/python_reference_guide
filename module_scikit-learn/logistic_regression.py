'''
This script contains examples of Logistic Regression analysis, using the
SciKit-Learn library.

Logistic regression is useful when trying to classify data between 2 binary
groups / labels. For example, a logistic model would be useful to predict if
someone has a disease (1) or does not have a disease (0).

Logistic regression uses the sigmoid function, which can only output between
0 - 1.
'''

import pathlib2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# Data is from here: https://www.kaggle.com/c/titanic/data
csv_url = ('https://raw.githubusercontent.com/robert-g-butler/python_reference'
           '_guide/master/dummy_data/logistic_dummy_data.csv')

df = pd.read_csv(csv_url)

# Explore the data with graphs ------------------------------------------------

df.head()
df.info()

sns.set_style(style='whitegrid')
sns.heatmap(data=df.isna(), cmap='viridis')  # yticklabels=False, cbar=False
plt.show()

sns.countplot(x='Survived', data=df, hue='Sex', palette='RdBu_r'); plt.show()
sns.countplot(x='Survived', data=df, hue='Pclass'); plt.show()
sns.distplot(df['Age'].dropna(), bins=30); plt.show()  # kde=False
sns.countplot(x='SibSp', data=df); plt.show()
df['Fare'].hist(bins=40, figsize=(10, 4)); plt.show()

# Clean missing values --------------------------------------------------------

# Clean missing Age values. Impute Age by Pclass.
sns.boxplot(x='Pclass', y='Age', data=df); plt.show()

sns.heatmap(data=df.isna(), cmap='viridis'); plt.show()

def impute_age(cols):
    age = cols['Age']
    pclass = cols['Pclass']
    if pd.isna(age):
        if pclass == 1:
            return 37
        elif pclass == 2:
            return 29
        else:
            return 24
    else:
        return age

df['Age'] = df[['Age', 'Pclass']].apply(func=impute_age, axis=1)

sns.heatmap(data=df.isna(), cmap='viridis'); plt.show()

# Drop the Cabin variable because there are too many missing values.
df.drop(columns='Cabin', axis=1, inplace=True)
sns.heatmap(data=df.isna(), cmap='viridis'); plt.show()

# Drop any remaining rows with missing values.
df.dropna(inplace=True)
sns.heatmap(data=df.isna(), cmap='viridis'); plt.show()

# Update text & categorical columns with numerical data -----------------------

# Get numerical values for each text column.
pd.get_dummies(df['Sex'])

# We must use 'drop_first' to avoid having 1 column perfectly the others.
# This problem is called 'multi-colinearity'.
sex = pd.get_dummies(df['Sex'], drop_first=True)
embarked = pd.get_dummies(df['Embarked'], drop_first=True)

df = pd.concat([df, sex, embarked], axis=1)
df.head()

# Drop columns that are text or aren't useful for prediction.
df.drop(['PassengerId', 'Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)
df.head()

# Create the model ------------------------------------------------------------

X = df.drop('Survived', axis=1)
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25)

logmodel = LogisticRegression()
logmodel.fit(X=X_train, y=y_train)

predictions = logmodel.predict(X=X_test)

# Check the prediction accuracy with 'classification_report'
print(metrics.classification_report(y_true=y_test, y_pred=predictions))

# Check the prediction accuracy with a 'confusion_matrix'
metrics.confusion_matrix(y_true=y_test, y_pred=predictions)


