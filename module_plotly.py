
'''
This script contains examples of functions that can be used from the Plotly
module.
'''

import pandas as pd
import numpy as np
import plotly
import plotly.offline as offl
import plotly.graph_objs as go

print(plotly.__version__)

df1 = pd.DataFrame(np.random.randn(100,4), columns=list('ABCD')); df1.head()
df2 = pd.DataFrame({'Categories':list('ABC'), 'Values':[32,43,50]}); df2
df3 = pd.DataFrame({'x':[1,2,3,4,5], 'y':[10,20,30,20,10], 'z':[500,400,300,200,100]}); df3
df4 = pd.DataFrame({'x':[1,2,3,4,5], 'y':[10,20,30,20,10], 'z':[5,4,3,2,1]}); df4

# Intro Example
fig = go.Figure(data=[{'type':'scatter', 'y':[2,1,4]}])
offl.plot(fig)

trace0 = go.Scatter(x=[1,2,3,4], y=[10,15,13,17])
trace1 = go.Scatter(x=[1,2,3,4], y=[16,5,11,9])
traces = [trace0,trace1]
offl.plot(traces)
offl.plot({'data':traces, 'layout':go.Layout(title='Simple Plot!')})  # More concise with 'layout':{'title':'TITLE'}

# Standard Graphs ------------------------------------------------------------

# Line Plots
df1.plot()
traces = [go.Scatter({'x':df1.index,
                      'y':df1[col],
                      'name':col}) for col in df1]
offl.plot({'data':traces,
           'layout':{'title':'Line Plot',
                     'xaxis':{'title':'x-axis'},
                     'yaxis':{'title':'y-axis'}}})

# Scatter Plots
traces1 = [go.Scatter({'x':df1['A'], 'y':df1['B']})]
offl.plot(traces1)
traces2 = [go.Scatter({'x':df1['A'], 'y':df1['B'], 'mode':'markers'})]
offl.plot(traces2)    
traces3 = [go.Scatter({'x':df1['A'], 'y':df1['B'], 'mode':'markers', 'marker':{'size':20}})]
offl.plot(traces3)

# Bar Plots
traces = [go.Bar({'x':df2['Categories'], 'y':df2['Values']})]
offl.plot(traces)

traces = [go.Bar({'x':df1.index, 'y':df1[col]}) for col in df1]
offl.plot(traces)

traces = [go.Bar({'x':df1.columns, 'y':df1.sum()})]
offl.plot(traces)

# Boxplots
traces = [go.Box({'y':df1[col]}) for col in df1]
offl.plot(traces)

# 3-D Plots
traces = [go.Surface({'z':df3.values})]  # .values turns data into a matrix.
offl.plot(traces)
traces = [go.Surface({'z':df4.values})]
offl.plot(traces)
traces = [go.Surface({'z':df4.values, 'colorscale':'Viridis'})]
offl.plot(traces)

# Histograms
traces = [go.Histogram({'x':df1['A']})]
offl.plot(traces)
traces = [go.Histogram({'x':df1['A'], 'nbinsx':50})]
offl.plot(traces)

traces = [go.Histogram({'x':df1[col]}) for col in df1]
offl.plot(traces)
offl.plot({'data':traces, 'layout':{'barmode':'overlay'}})

# Bubble Plots
traces = [go.Scatter({'x':df1['A'], 'y':df1['B'], 'mode':'markers', 'marker':{'size':abs(df1['C'])*50}})]
offl.plot(traces)

# Scatter Matrix
traces = [go.Splom({'dimensions':[{'label':col, 'values':df1[col]} for col in df1]})]
offl.plot(traces)

# Geographic (Choropleth) Maps -----------------------------------------------

import plotly.offline as offl
import plotly.graph_objs as go
import pandas as pd
str_inDir = 'C:/Users/robbi/Dropbox/Work & Learning/Language - Python/Udemy - Python for Data Science and Machine Learning/Refactored_Py_DS_ML_Bootcamp-master/09-Geographical-Plotting/'

# USA State Example Plot
data = [{'type':'choropleth',
        'locations':['AZ','CA','NY'],
        'locationmode':'USA-states',  # LOCATIONMODE = Graphing mode
        'colorscale':'Portland',
        'text':['text 1','text 2','text 3'],  # TEXT = Hover-over text
        'z':[1,2,3],  # Z = Value to line up each item to the colorbar
        'colorbar':{'title':'Colorbar Title'}}]
layout = {'geo':{'scope':'usa'}}
fig = go.Figure(data=data, layout=layout)
offl.plot(fig)

# USA State Agricultural Plot
df_agri = pd.read_csv(str_inDir+'2011_US_AGRI_Exports')
df_agri.head()
df_agri.info()

data = [{'type':'choropleth',
         'colorscale':'YlOrRd',
         'locationmode':'USA-states',
         'locations':df_agri['code'],
         'z':df_agri['total exports'],
         'text':df_agri['text'],
         'colorbar':{'title':'Millions USD'},
         'marker':{'line':{'color':'rgb(255,255,255)',
                           'width':2}}}]
layout = {'title':'2011 US Agriculture Exports by State',
          'geo':{'scope':'usa',
                 'showlakes':True,
                 'lakecolor':'rgb(85,173,240)'}}
fig = go.Figure(data=data, layout=layout)
offl.plot(fig)

# Global GDP Plot
df_gdp = pd.read_csv(str_inDir+'2014_World_GDP')
df_gdp.head()

data = [{'type':'choropleth',
         'locations':df_gdp['CODE'],
         'z':df_gdp['GDP (BILLIONS)'],
         'text':df_gdp['COUNTRY'],
         'colorbar':{'title':'Billions USD'}}]
layout = {'title':'2014 Global GDP',
          'geo':{'showframe':False,
                 'projection':{'type':'natural earth'}}}
fig = go.Figure(data=data, layout=layout)
offl.plot(fig)
