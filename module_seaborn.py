
'''
This script contains examples of functions that can be used from the Seaborn
module.
'''

import seaborn as sb
import numpy as np
import statistics
import matplotlib.pyplot as plt

# Distribution Plots ---------------------------------------------------------

from scipy.stats import spearmanr, pearsonr

tips = sb.load_dataset('tips')
tips.head()

# Distribution Plots
sb.distplot(a=tips['total_bill'])
sb.distplot(a=tips['total_bill'], kde=False)
sb.distplot(a=tips['total_bill'], kde=False, bins=30)

# KDE Plot (Kernel Density Estimate)
sb.kdeplot(data=tips['total_bill'])

# Line Plots
sb.lineplot(x='total_bill', y='size', data=tips)
sb.lineplot(x='size', y='total_bill', data=tips)

# Joint Plots
sb.jointplot(x='total_bill', y='tip', data=tips)
sb.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
sb.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
sb.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
sb.jointplot(x='total_bill', y='tip', data=tips, stat_func=pearsonr)  # Linear relation
sb.jointplot(x='total_bill', y='tip', data=tips, stat_func=spearmanr)  # Monotone relation
sb.jointplot(x='total_bill', y='tip', data=tips).plot_joint(sb.kdeplot, n_levels=6)
sb.jointplot(x='total_bill', y='tip', data=tips).plot_joint(sb.kdeplot, n_levels=6).plot_marginals(sb.rugplot)

# Pair Plots
sb.pairplot(data=tips)
sb.pairplot(data=tips, hue='sex')  # Hue splits the data by a categorical column
sb.pairplot(data=tips, hue='sex', palette='coolwarm')

# Rug Plots
sb.rugplot(a=tips['total_bill'])

# Categorical Plots ----------------------------------------------------------

tips = sb.load_dataset('tips')
tips.head()

# Barplots
sb.barplot(x='total_bill', y='sex', data=tips)
sb.barplot(x='sex', y='total_bill', data=tips)
sb.barplot(x='sex', y='total_bill', data=tips, estimator=statistics.mean)  # Default lines is 'mean'
sb.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)  # You can add other stats for line

# Count Plots
sb.countplot(x='sex', data=tips)

# Boxplots
sb.boxplot(x='day', y='total_bill', data=tips)
sb.boxplot(x='day', y='total_bill', data=tips, hue='smoker')  # Split by hue category

# Violin Plots
sb.violinplot(x='day', y='total_bill', data=tips)
sb.violinplot(x='day', y='total_bill', data=tips, hue='sex')  # Split by hue category
sb.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)  # Graph on each side of plot

# Strip Plots
sb.stripplot(x='day', y='total_bill', data=tips)
sb.stripplot(x='day', y='total_bill', data=tips, jitter=True)
sb.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex')
sb.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', split=True)

# Swarm Plots
sb.swarmplot(x='day', y='total_bill', data=tips)

# Violin & Swarm Plots
sb.violinplot(x='day', y='total_bill', data=tips); sb.swarmplot(x='day', y='total_bill', data=tips, color='black')

# Factor Plots (General-Purpose with Kind Specification)
sb.factorplot(x='day', y='total_bill', data=tips)
sb.factorplot(x='day', y='total_bill', data=tips, kind='box')
sb.factorplot(x='day', y='total_bill', data=tips, kind='bar')
sb.factorplot(x='day', y='total_bill', data=tips, kind='violin')
sb.factorplot(x='day', y='total_bill', data=tips, kind='strip')
sb.factorplot(x='day', y='total_bill', data=tips, kind='swarm')

# Matrix Plots ---------------------------------------------------------------

tips = sb.load_dataset('tips')
tips.head()
flights = sb.load_dataset('flights')
flights.head()

tips.head()
tips.corr()

# Heatmaps
sb.heatmap(data=tips.corr())
sb.heatmap(data=tips.corr(), annot=True)
sb.heatmap(data=tips.corr(), annot=True, cmap='coolwarm')

flights.head()
flights_pivoted = flights.pivot_table(values='passengers', index='month', columns='year')
flights_pivoted.head()

sb.heatmap(data=flights_pivoted)
sb.heatmap(data=flights_pivoted, cmap='magma')
sb.heatmap(data=flights_pivoted, cmap='magma', linecolor='white', linewidths=1)

# Cluster Maps
sb.clustermap(data=flights_pivoted)
sb.clustermap(data=flights_pivoted, cmap='coolwarm')
sb.clustermap(data=flights_pivoted, cmap='coolwarm', standard_scale=1)

# Grid Plots -----------------------------------------------------------------

tips = sb.load_dataset('tips')
tips.head()
iris = sb.load_dataset('iris')
iris.head()
iris['species'].unique()
sb.pairplot(data=iris)

# PairGrid
sb.PairGrid(data=iris)
g = sb.PairGrid(data=iris).map(func=plt.scatter)
g = sb.PairGrid(data=iris).map_diag(func=sb.distplot)
g = sb.PairGrid(data=iris).map_diag(func=sb.distplot).map_upper(func=plt.scatter)
g = sb.PairGrid(data=iris).map_diag(func=sb.distplot).map_upper(func=plt.scatter).map_lower(func=sb.kdeplot)

# FacetGrid
g = sb.FacetGrid(data=tips, col='time', row='smoker').map(sb.distplot, 'total_bill')
g = sb.FacetGrid(data=tips, col='time', row='smoker').map(sb.scatterplot, 'total_bill', 'tip')

# Regression Plots -----------------------------------------------------------

tips = sb.load_dataset('tips')
tips.head()

# Linear Model Plots
sb.lmplot(x='total_bill', y='tip', data=tips)
sb.lmplot(x='total_bill', y='tip', data=tips, hue='sex')
sb.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['^','1'])
sb.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['^','1'], scatter_kws={'s':100})

sb.lmplot(x='total_bill', y='tip', data=tips)
sb.lmplot(x='total_bill', y='tip', data=tips, col='time')
sb.lmplot(x='total_bill', y='tip', data=tips, col='time', row='day')
sb.lmplot(x='total_bill', y='tip', data=tips, col='time', row='day', hue='sex')
sb.lmplot(x='total_bill', y='tip', data=tips, col='time', row='day', hue='sex', aspect=.6)
sb.lmplot(x='total_bill', y='tip', data=tips, col='time', row='day', hue='sex', aspect=.6, size=4)

# Style & Color --------------------------------------------------------------

tips = sb.load_dataset('tips')
tips.head()

# Styles
sb.set_style(style='white'); sb.countplot(x='sex', data=tips)
sb.set_style(style='ticks'); sb.countplot(x='sex', data=tips)
sb.set_style(style='darkgrid'); sb.countplot(x='sex', data=tips)
sb.set_style(style='whitegrid'); sb.countplot(x='sex', data=tips)
sb.set_style(style='dark'); sb.countplot(x='sex', data=tips)

# Despine
sb.set_style(style='ticks')
sb.countplot(x='sex', data=tips)
sb.countplot(x='sex', data=tips); sb.despine(top=True, right=True, left=True, bottom=True)

# Setting Size
plt.figure(figsize=(12,3)); sb.countplot(x='sex', data=tips)

# Setting Context
sb.set_context(context='poster'); sb.countplot(x='sex', data=tips)
sb.set_context(context='poster', font_scale=3); sb.countplot(x='sex', data=tips)
sb.set_context(context='notebook'); sb.countplot(x='sex', data=tips)

# Palette (google: "matplotlib colormaps")
sb.lmplot(x='total_bill', y='tip', data=tips)
sb.lmplot(x='total_bill', y='tip', data=tips, hue='sex')
sb.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm')
sb.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='seismic')

# Move Legend
sb.violinplot(x='day', y='total_bill', data=tips, hue='sex')
plt.legend(bbox_to_anchor=(1,.5), loc=6)