'''
This script contains examples of Linear Regression analysis, using the SciKit-
Learn library.

Linear regression is useful when trying to predict from a set of continuous
data.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_boston

boston = load_boston()
df = pd.DataFrame(data=boston['data'], columns=boston['feature_names'])
df['target'] = pd.Series(boston['target'])

df.columns
df.info()
df.describe()
df.head()

sns.pairplot(df)
plt.show()

sns.distplot(df['target']); plt.show()
sns.heatmap(df.corr(), annot=True, cmap='viridis'); plt.show()

# Set X and y
X = df[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT']]
y = df['target']

# Split for test and train ----------------------------------------------------
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.4,
                                                    random_state=101)

# Make and fit the model ------------------------------------------------------
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X=X_train, y=y_train)

# Check out the intercept & coefficients of each variable.
lm.intercept_
lm.coef_

df_coef = pd.DataFrame(data=lm.coef_, index=X_train.columns, columns=['coef'])
df_coef

# Check predictions
predictions = lm.predict(X=X_test)

plt.scatter(y_test, predictions)
plt.show()

# Check residuals (Normally distributed residuals means that the model was the correct choice for the data)
sns.distplot((y_test-predictions))
plt.show()

# Evaluation Metrics (Try to minimize all of these) ---------------------------

#   1. Mean Absolute Error (MAE)  -  Simple straight error
#   2. Mean Squared Error (MSE)  -  Squares means that outliers are more visible
#   3. Root Mean Squared Error (RMSE)  -  Allows RMSE results to be interpreted in "y" units.

from sklearn import metrics

metrics.mean_absolute_error(y_true=y_test, y_pred=predictions)
metrics.mean_squared_error(y_true=y_test, y_pred=predictions)
np.sqrt(metrics.mean_squared_error(y_true=y_test, y_pred=predictions))

# Check the R^2 score.
metrics.explained_variance_score(y_true=y_test, y_pred=predictions)

lm.score(X=X_test, y=y_test)


