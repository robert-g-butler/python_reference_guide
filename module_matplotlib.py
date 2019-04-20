
'''
This script contains examples of functions that can be used from the
MatplotLib module.
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(start=1, stop=5, num=11)
y = x**2

# Functional Method of Plotting (BAD) ----------------------------------------

# Make a simple plot.
plt.plot(x, y)

# Make a plot with more settings.
plt.plot(x, y, 'r');  # Color line red.
plt.plot(x, y, 'r'); plt.xlabel('X Label');  # X-label
plt.plot(x, y, 'r'); plt.xlabel('X Label'); plt.ylabel('Y Label');  # Y-label
plt.plot(x, y, 'r'); plt.xlabel('X Label'); plt.ylabel('Y Label'); plt.title('Title')  # Title

# Make adjacent subplots.
plt.subplot(1,2,1); plt.plot(x,y,'r'); plt.subplot(1,2,2); plt.plot(y,x,'b')

# Object Oriented (OO) Method of Plotting (GOOD) ----------------------------------

# Make a simple plot
plot_1 = plt.figure()
plot_1
axes = plot_1.add_axes([.1,.1,.8,.8])
plot_1
axes.plot(x,y)
plot_1
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Graph Title')
plot_1

# Make an inception plot
plot_2 = plt.figure()
axes1 = plot_2.add_axes([.1,.1,.8,.8])
axes2 = plot_2.add_axes([.2,.5,.4,.3])
plot_2
axes1.plot(x,y)
axes2.plot(y,x)
plot_2
axes1.set_title('BIG')
axes2.set_title('SMALL')
plot_2

# Making Subplots with OO Plotting
fig, axes = plt.subplots(nrows=1, ncols=2)  # subplots() is just a multi-axes wrapper for figure()
fig
axes
for ax in axes:
    ax.plot(x,y)
fig
axes[0].plot(x,y)
axes[1].plot(y,x)
fig
axes[0].set_title('1st')
axes[1].set_title('2nd')
fig

# Setting Size and DPI, and Saving.
fig = plt.figure(figsize=(8,2), dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
fig

fig,axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2), dpi=100)
axes[0].plot(x,y)
axes[1].plot(y,x)
fig.tight_layout()
fig
fig.savefig('C:/Users/robbi/Dropbox/Work & Learning/Language - Python/test.png')

# Add Legends
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,x**2, label='x^2')
axes.plot(x,x**3, label='x^3')
axes.legend(loc=0)  # Positioned with a code.
fig

axes.legend(loc=(1.03,.88))  # Positioned with a direct placement.
fig

# Adjusting Lines
fig,axes = plt.subplots(nrows=1, ncols=3)
fig.tight_layout()
axes[0].plot(x,y, color='red', lw=20, alpha=.3, ls=':')
axes[1].plot(x,y, color='#00ff00', lw=3, alpha=.3, ls='--')
axes[2].plot(x,y, color='blue', ls='steps')
fig

# Adjusting Markers
fig,axes = plt.subplots(nrows=1, ncols=3)
fig.tight_layout()
axes[0].plot(x,y, color='red', lw=.5, marker='o', markersize=5)
axes[1].plot(x,y, color='#00ff00', lw=.5, marker='2', markersize=15)
axes[2].plot(x,y, color='blue', lw=.5, marker='x', markersize=15)
fig

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y, color='red', marker='o', markersize=20,
    markerfacecolor='yellow', markeredgewidth=3, markeredgecolor='orange')
fig

# Set Plot Limits
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y)
axes.set_xlim([1.5,3.5])
axes.set_ylim([2,15])
fig

