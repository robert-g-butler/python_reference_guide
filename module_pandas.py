
'''
This script contains examples of functions that can be used from the Pandas
module.
'''

# Series ---------------------------------------------------------------------

import pandas as pd
import numpy as np

# Creating series
pd.Series(data=[1,2,3,4])                           # list
pd.Series(data=[1,2,3,4], index=['a','b','c','d'])  # custom index
pd.Series(data={'a':1, 'b':2, 'c':3, 'd':4})        # dictionary

# Indexing series
ser_1 = pd.Series(data=[1,2,3,4], index=['a','b','c','d']); ser_1
ser_1['b']
ser_1[2]

# Joining Series
ser_1 = pd.Series(data=[1,2,3,4], index=['a','b','c','d']); ser_1
ser_2 = pd.Series(data=[1,2,5,4], index=['a','b','e','d']); ser_2
ser_1 + ser_2

# NOTE: Pandas joins series by INDEX. This is why there are 2 NaN values.

# DataFrames - Basics --------------------------------------------------------

import pandas as pd
import numpy as np

df_a = pd.DataFrame({'A': list(range(43))[-6:],
                     'B': [pd.Timestamp('20180725')] * 5 + [None],
                     'C': ['cat', 'dog', 'fish', None, 'bird', 'snail'],
                     'D': [2/3, 1/2, None, 8/3, 1/9, 6/2]})
df_b = pd.DataFrame(data=np.random.randn(6, 4),
                    index=pd.date_range(start = '20180621', periods = 6),
                    columns=['col{}'.format(num) for num in list('1234')])
df_a
df_b

# Column types
df_a.dtypes
df_b.dtypes
df_a.head()
df_a.tail()
df_a.index
df_b.index
df_b.reset_index()
df_a.columns
df_b.columns
df_a.values
df_b.values
df_b.shift(periods = 1)
df_b.sub(100)
df_b.add(100)
df_a.info()
df_a.describe()  # Summary Metrics
df_a.T  # Transpose
df_a.transpose()  # Same thing as T
df_b.sort_index(axis = 1, ascending = False)  # Sort column or row order
df_b.sort_values(by = 'col2', ascending = True)  # Sort rows

# DataFrames - Selecting -----------------------------------------------------

import pandas as pd
import numpy as np

# Select Columns
df_b.col1  # NOTE: Don't use this way b/c it will be confused with methods.
df_b['col1']
df_b[['col1', 'col3']]

# Select Rows
df_b[:3]
df_b['20180623':'20180625']

# .loc - Select by INDEX (Label)
df_a
df_b
df_a.loc[2]  # row @ index 2
df_b.loc['20180623']  # row @ index '20180623'
df_b.loc[:, ['col1', 'col3']]
df_b.loc['20180623':'20180625', ['col1', 'col3']]
df_a.loc[3, 'C']
df_a.at[3, 'C']  # .at is faster than .loc for single values

df_a.loc[df_a['D'].idxmax()]
df_a.loc[df_a['D'].idxmin()]

# .iloc - Select by POSITION
df_a.iloc[3]  # Slice of 3rd row
df_a.iloc[3:5, :2]
df_a.iloc[[1, 4], [0, 2]]
df_a.iloc[1:3, :]
df_a.iloc[2, 2]
df_a.iat[2, 2]  # .iat is faster than .iloc for single values

# Boolean Indexing & Filtering
df_b
df_b[df_b>0]
df_b[df_b['col1']<0]
df_b[(df_b['col1']>0) & (df_b['col2']<0)]  # Filtering by 2 columns (and)
df_b[(df_b['col1']>0) | (df_b['col2']<0)]  # Filtering by 2 columns (or)
df_a[df_a['C'].isin(['fish', 'bird'])]

# String Functions
series_a = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
series_a.str.lower()
series_a.str.upper()

# DataFrames - Sorting -------------------------------------------------------

import pandas as pd
import numpy as np

df_a
df_a.sort_values(by='C')
df_a.sort_values(by=['B','D'], axis=0, ascending=[True,False])

# DataFrames - Creating & Modifying Columns & Rows ---------------------------

# Creating Columns
df_a['E'] = df_a['A']; df_a

# Rename Columns
df_a.rename(columns = {'A':'col_a', 'B':'col_b', 'C':'col_c', 'D':'col_d'})

# Reset & Set Index
df_c = df_b.copy(); df_c
df_c.reset_index()
df_c  # Reset did not set in place. Use 'inplace=True' for that.
df_c.reset_index(inplace=True); df_c

df_c.loc[:, 'States'] = pd.Series('CA NY WY OR CO TX'.split()); df_c
df_c.set_index('States')

# Dropping Columns
df_a['E'] = df_a['A']; df_a
df_a.drop(labels='E', axis=1)  # Doesn't affect original table
df_a
df_a.drop(labels='E', axis=1, inplace=True); df_a  # Affects original table

# Dropping Rows
df_a.drop(labels=2, axis=0)  # Doesn't affect original table
df_a
df_a.drop(labels=2, axis=0, inplace=True); df_a  # Affects original table

# Replace column values
df_a['C'].replace(['cat', 'dog', 'fish'], ['kittie', 'doggie', 'fishie'])

# DataFrames - Missing Values ------------------------------------------------

import pandas as pd
import numpy as np

# Create dataframe with missing values (NaN)
df_miss = pd.DataFrame({'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]}); df_miss

# Find missing values
df_miss.isna()
df_miss.isnull()  # same as .isna()

# Drop missing values
df_miss.dropna(axis=0)
df_miss.dropna(axis=1)
df_miss.dropna(axis=0, thresh=2)
df_miss.dropna(axis=0, how = 'any')
df_miss.dropna(axis=0, how = 'all')

# Fill missing values
df_miss.fillna(value='FILLED')
df_miss['A'].fillna(value=df_miss['A'].mean())  # Fill w/ mean to avoid skewing data

# DataFrames - Multi-Level Indexes -------------------------------------------

import pandas as pd
import numpy as np

# Create multi-level index
multi_index = list(zip(((['G1']*3) + (['G2']*3)), [1,2,3,1,2,3])); multi_index
multi_index = pd.MultiIndex.from_tuples(multi_index); multi_index

# Create multi-level dataframe
df_multi = pd.DataFrame(data=np.random.rand(6,2), index = multi_index, columns=['A','B']); df_multi

# Select data from multi-level dataframe
df_multi.loc['G1']
df_multi.loc['G1'].loc[:, ['A']]
df_multi.loc['G2'].loc[1,'B']

# Get & Set index names
df_multi.index.names
df_multi.index.names = ['lvl1','lvl2']; df_multi

# Get cross sections of multi-level index
df_multi.xs(key='G1', level='lvl1')
df_multi.xs(key=1, level='lvl2')  # can select data from any level, which is better than loc for multi-level DFs.

# DataFrames - Math, Statistics, & Operations --------------------------------

import pandas as pd
import numpy as np

# Stats
df_b['col1'].count() # Row count
df_b.mean()  # Mean on y-axis
df_b.mean(axis=1)  # Mean on x-axis
df_b.shift(periods=1)
df_b

# Unique Values
df_c = pd.DataFrame(data=np.random.randint(low=11, high=14, size=(20,4)), columns=list('abcd')); df_c
df_c['b'].unique()  # unique values
df_c['b'].nunique()  # # of unique values
df_c['b'].value_counts()  # count of unique values

# Apply
df_apply = pd.DataFrame({'A':[1,2,3,4,5,6], 'B':[2,4,6,8,10,12], 'C':np.random.rand(6)}); df_apply

df_apply.apply(np.sqrt)  # apply built-in function across all elements
df_apply.apply(lambda x: x**x)  # apply custom function across elements

df_apply.apply(lambda x: x.max() - x.min(), axis=0)  # apply aggregate function across index
df_apply.apply(lambda x: x.max() - x.min(), axis=1)  # apply aggregate function across columns
df_apply['NewCol'] = df_apply['B'].apply(lambda x: 'I yam '+str(x)+' years old.')

# Map
df_map = pd.DataFrame({'DayNum':np.random.randint(0,7,20)}); df_map
dict_numToDay = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}
df_map['Day'] = df_map['DayNum'].map(dict_numToDay); df_map

# Cumulative Sum
df_apply[['A','B','C']].cumsum()

# Correlation between variables
df_apply[['A','C']].corr()

# DataFrames - Group Functions -----------------------------------------------

import pandas as pd
import numpy as np

# Grouping
df_c = pd.DataFrame({'col1': list('AAAAAABBBBBBCCCCCC'),
                     'col2': list('IIJJKKIIJJKKIIJJKK'),
                     'col3': np.random.randn(18),
                     'col4': np.random.randn(18)})
df_c

# Groupby Functions
df_c.groupby('col2').std()
df_c.groupby('col1').sum()
df_c.groupby('col1').max()
df_c.groupby('col1').min()
df_c.groupby('col1', as_index=False).sum()
df_c.groupby('col2', as_index=False).mean()
df_c.groupby(['col1','col2'], as_index=False).sum()
df_c.groupby(['col1','col2'], as_index=False)['col4'].sum()
df_c['col5'] = df_c.groupby(['col1','col2'], as_index=False)['col4'].transform('sum')

# NOTE: Transform doesn't 'squish' rows by group.

# Summary statistict
df_c.groupby('col1').describe()
df_c.groupby('col1').describe().transpose()
    

# DataFrames - Merging -------------------------------------------------------

import pandas as pd
import numpy as np

# Make example dataframes
df_a = pd.DataFrame({'A':[1,2,3,4,5,6],
                     'B':'G1 G1 G1 G2 G2 G2'.split(),
                     'C':list(np.random.randint(low=10, size=6)),
                     'D':list(np.random.randint(low=10, size=6))}); df_a
df_b = pd.DataFrame({'A':[0,2,4,6,8,10],
                     'B':'G1 G1 G1 G2 G2 G2'.split(),
                     'E':list(np.random.randint(low=10, size=6)),
                     'F':list(np.random.randint(low=10, size=6))}); df_b

# Merging Vertically
pd.concat([df_a, df_b])
df_a.append(other=df_b)

# NOTE: There are no major differences between pd.concat() vs df.append()

# Merge Horizontally with Merge
df_a
df_b
pd.merge(left=df_a, right=df_b, how='outer', on='A')
pd.merge(left=df_a, right=df_b, how='left', on='A')
pd.merge(left=df_a, right=df_b, how='right', on='A')
pd.merge(left=df_a, right=df_b, how='inner', on='A')
pd.merge(left=df_a, right=df_b, how='outer', left_on=['A','B'], right_on=['A','B'])

# Merge Horizontally with Join
df_a.join(other=df_b.loc[:,['E','F']])  # Joins on index

# DataFrames - Pivoting ------------------------------------------------------

import pandas as pd
import numpy as np

# Pivot Table
df_a = pd.DataFrame({'A':['foo','foo','foo','bar','bar','bar'],'B':['one','one','two','two','one','one'],'C':list('xyxyxy'),'D':list(range(6))}); df_a
df_a.pivot_table(values='D', index=['A','B'], columns='C')

# Unstack
index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'), ('two', 'a'), ('two', 'b')])
df_b = pd.Series(np.arange(1.0, 5.0), index=index); df_b

df_b.unstack(level=-1)

df_b.unstack(level=0)

df_b.unstack(level=0).unstack()  # Reverts it

# T
df_c = pd.DataFrame({'A':list(range(5)), 'B':np.random.randn(5), 'C':list('abcde')}); df_c
df_c.T
df_c.transpose()  # Same thing

# DataFrames - Reading & Writing Files ---------------------------------------

import pandas as pd
import numpy as np

str_inDir = 'C:/Users/robbi/Dropbox/Work & Learning/Language - Python/Udemy - Python for Data Science and Machine Learning/Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/'

# CSV
df_csv = pd.read_csv(str_inDir+'example')
df_csv.to_csv(str_inDir+'OUTPUT_EXAMPLE.csv', index=False)

# Excel (No formulas, images, macros)
df_excel = pd.read_excel(io=str_inDir+'Excel_Sample.xlsx', sheet_name='Sheet1')
df_excel.to_excel(str_inDir+'OUTPUT_EXAMPLE.xlsx', sheet_name='Output', index=False)

# HTML
df_html = pd.read_html(io='http://www.fdic.gov/bank/individual/failed/banklist.html')
type(df_html)  # Pandas made a list of all tables in the website.
df_html[0]

# SQL (NOTE: It's better to use a dedicated package for reading SQL)
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')  # Create a temp SQL engine in memory
pd.DataFrame(data=np.random.rand(5,5), columns=list('ABCDE')).to_sql(name='TMP_SQL_TABLE', con=engine, index=False)
pd.read_sql(sql='TMP_SQL_TABLE', con=engine)

# Pandas Graphing ------------------------------------------------------------

import numpy as np
import pandas as pd

str_inDir = 'C:/Users/robbi/Dropbox/Work & Learning/Language - Python/Udemy - Python for Data Science and Machine Learning/Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/'
df1 = pd.read_csv(str_inDir+'df1', index_col=0); df1.head()
df2 = pd.read_csv(str_inDir+'df2'); df2.head()
df3 = pd.read_csv(str_inDir+'df3'); df3.head()

# Histograms
df1.hist()
df1['A'].hist()
df1['A'].hist(bins=30)

df1['A'].plot(kind='hist')
df1['A'].plot(kind='hist', bins=30)

df1['A'].plot.hist()
df1['A'].plot.hist(bins=30)

# Area Plots
df2.plot.area()
df2.plot.area(alpha=.4)

# Bar Plots
df2.plot.bar()
df2.plot.bar(stacked=True)

# Line Plots
df1.plot.line()
df1.plot.line(y='B')
df1.plot.line(y='B', figsize=(12,3))
df1.plot.line(y='B', figsize=(12,3), lw=1)

# Scatter Plots
df1.plot.scatter(x='A', y='B')
df1.plot.scatter(x='A', y='B', c='C')
df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm')
df1.plot.scatter(x='A', y='B', s=df1['C'])
df1.plot.scatter(x='A', y='B', s=df1['C']*100)

# Boxplots
df1.plot.box()

# Bivariate Plots
df4 = pd.DataFrame(np.random.randn(1000,2), columns=['a','b'])
df4.head()
df4.plot.hexbin(x='a', y='b')
df4.plot.hexbin(x='a', y='b', gridsize=25)
df4.plot.hexbin(x='a', y='b', gridsize=25, cmap='coolwarm')

# Kernel Density Estimate Plots
df2.plot.kde()
df2['a'].plot.kde()

df2.plot.density()
df2['a'].plot.density()

