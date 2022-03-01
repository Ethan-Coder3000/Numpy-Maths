import numpy as np

# Make the array `my_array`
x = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)
y = np.array([[4,3,2,1], [9,8,7,6]], dtype=np.int64)

# Add
np.add(x,y)

# Subtract
np.subtract(x,y)

# Multiply
np.multiply(x,y)

# Divide 
np.divide(x,y)

# Calculate the remainder
np.remainder(x,y)

# Matrix multiplication
x.dot(y)
