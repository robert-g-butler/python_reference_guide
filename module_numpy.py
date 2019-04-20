
'''
This script contains examples of functions that can be used from the NumPy
module.
'''

# Import
import numpy as np

# Create Arrays of 0s and 1s
np.zeros(shape=5)      # vector (1-D with [ ])
np.zeros(shape=(3,5))  # matrix (2-D with [ [],[] ])
np.ones(shape=5)       # vector
np.ones(shape=(3,5))   # matrix

# Create arrays from NumPy methods
np.arange(start=0, stop=100, step=5)   # 1-D
np.linspace(start=0, stop=10, num=21)  # 1-D
np.eye(N=5)                            # 2-D identity matrix (linear algebra)

# Create random arrays
np.random.rand()     # Random float between 0-1
np.random.rand(5)
np.random.rand(5,5)
np.random.randn()    # Random float in normal distribution around 0
np.random.randn(5)
np.random.randn(5,5)
np.random.randint(low=0, high=100)  # Random integer between low - high
np.random.randint(low=0, high=100, size=5)
np.random.randint(low=0, high=100, size=(5,5))

# Reshape arrays
arr_1x24 = np.random.rand(24); arr_1x24
np.reshape(a=arr_1x24, newshape=24)
np.reshape(a=arr_1x24, newshape=(2,12))
np.reshape(a=arr_1x24, newshape=(3,8))
np.reshape(a=arr_1x24, newshape=(4,6))

arr_1x24.reshape(4,6)

# Create Arrays from lists
np.array( list(range(10)) )
np.array( [[1,2,3],[4,5,6],[7,8,9]] )

# Get info from array
arr_1 = np.random.randint(0,100,10); arr_1
arr_1.sum()
arr_1.std()
arr_1.max()
arr_1.min()
arr_1.mean()
arr_1.argmax()  # index of the max value
arr_1.argmin()  # index of the min value
arr_1.shape     # dimensions of the array
arr_1.dtype     # data type of array

np.sum(arr_1)
np.std(arr_1)
np.max(arr_1)
np.min(arr_1)
np.mean(arr_1)

# Slicing 1-D arrays
arr_1 = np.random.randint(0,100,10); arr_1
arr_1[3]
arr_1[-1]
arr_1[1:5]
arr_1[:5]
arr_1[5:]
arr_1[-3:]

# Slicing 2-D arrays
arr_1 = np.random.randint(0,100,(5,5)); arr_1
arr_1[3][1]
arr_1[-1][2]
arr_1[2,3]
arr_1[1:3,3:]
arr_1[:,1:2]

# Conditional selection
arr_1 = np.random.randint(0,100,10); arr_1
arr_2 = np.random.randint(0,100,(5,5)); arr_2
arr_1 > 50
arr_1[arr_1>50]

# Reassigning array values
arr_1 = np.random.randint(0,100,10); arr_1
arr_2 = arr_1[:5]; arr_2
arr_2[:] = 5
arr_2
arr_1

arr_3 = np.random.randint(0,100,10); arr_3
arr_4 = arr_3.copy()[:5]; arr_4
arr_4[:] = 5
arr_4
arr_3

# NOTE: A copy of arr_1 was not made. Any changes to reassigned elements will
#       affect the original array. NumPy.copy() fixes this.

# Universal Functions (Math & Operations)
arr_1 = np.arange(start=1, stop=101).reshape((10,10)); arr_1
arr_1 + 100
arr_1 + arr_1
arr_1 - 100
arr_1 - arr_1
arr_1 * 100
arr_1 * arr_1
arr_1 / 100
arr_1 / arr_1
np.sqrt(arr_1)
np.exp(arr_1)
np.log(arr_1)
np.sin(arr_1)
np.cos(arr_1)
np.tan(arr_1)
