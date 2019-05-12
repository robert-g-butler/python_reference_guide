'''
This script contains examples of K Nearest Neighbors analysis, using the
SciKit-Learn library.
'''

# Import data -----------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_url = ('https://raw.githubusercontent.com/robert-g-butler/python_reference'
           '_guide/master/dummy_data/knn_dummy_data.csv')

df = pd.read_csv(csv_url)
df.head()
df.info()
df.describe()

sns.pairplot(data=df, hue='TARGET CLASS',
             vars=df.drop('TARGET CLASS', axis=1).columns)
plt.show()

# Goal: Determine model to predict if a set of features belong to the
#       TARGET CLASS.

# Standardize feature scales --------------------------------------------------

# KNN looks at distance, so you should standardize all variables to have the
# same scale.

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X=df.drop('TARGET CLASS', axis=1))
scaled_features = scaler.transform(X=df.drop('TARGET CLASS', axis=1))

# Create a dataframe with standardized feature scales.
df_feat = pd.DataFrame(data=scaled_features, columns=df.columns[:-1])

# Show the difference between the standardized and unstandardized data frames.
sns.heatmap(df, cmap='viridis'); plt.show()
sns.heatmap(df_feat, cmap='viridis'); plt.show()

# Train Test Split ------------------------------------------------------------

from sklearn.model_selection import train_test_split

X = df_feat
y = df['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)

# Fit KNN model to data -------------------------------------------------------

from sklearn.neighbors import KNeighborsClassifier

# "n_neighbors" means "look at this many closest neighbors before predicting."
# Always choose an ODD n_neighbors when there are 2 CLASSES to avoid ties.

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X=X_train, y=y_train)
pred = knn.predict(X=X_test)

# Assess the model with metrics -----------------------------------------------

from sklearn import metrics

metrics.confusion_matrix(y_true=y_test, y_pred=pred)
print(metrics.classification_report(y_true=y_test, y_pred=pred))

# Average error rate
np.mean(pred != y_test)

# Assess many models with differnet K values (aka, "Elbow Method") ------------

error_rate = []

for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    _ = knn.fit(X=X_train, y=y_train)
    pred_i = knn.predict(X=X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10, 6))
plt.plot(range(1, 40), error_rate, color='blue', linestyle='dashed',
         marker='o', markerfacecolor='red', markersize=10)
plt.title('Error Rate vs K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()

# Chose the best K Value and run the model again ------------------------------

knn = KNeighborsClassifier(n_neighbors=17)
_ = knn.fit(X=X_train, y=y_train)
pred = knn.predict(X=X_test)

metrics.confusion_matrix(y_true=y_test, y_pred=pred)
print(metrics.classification_report(y_true=y_test, y_pred=pred))

