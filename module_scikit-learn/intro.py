
'''
This script contains examples of functions that can be used from the SciKit-
Learn module.
'''

# Example ------------------------------------------------------------

# Create test data
import numpy as np

X, y = np.arange(10).reshape((5, 2)), range(5)
X
y

# Split test data into train & test data frames.
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3,
                                                    random_state=42)
X_train
X_test
y_train
y_test

# Create the model
from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept=True, normalize=True, copy_X=True)
print(model)

# Fit the model
model.fit(X=X_train, y=y_train)
print(model)

# Predict values
predictions = model.predict(X=X_test)

# Check the accuracy of the predictions
model.score(X=X_test, y=y_test)

