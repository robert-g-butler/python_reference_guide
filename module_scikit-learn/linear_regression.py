'''
This script contains examples of Linear Regression analysis, using the SciKit-
Learn library.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

housing_csv = (r'C:\Users\robbi\Dropbox\Work & Learning\Programming\Language'
               r' - Python\Projects & Tutorials\Udemy - Python for Data '
               r'Science and Machine Learning\Refactored_Py_DS_ML_Bootcamp'
               r'-master\11-Linear-Regression\USA_Housing.csv')

df = pd.read_csv(housing_csv)
df.columns
df.info()
df.describe()

sns.pairplot(df)
plt.show()

sns.distplot(df['Price'])
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()



