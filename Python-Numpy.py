# Import NumPy
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Basic operations
print(arr + 2)
print(arr * 2)
print(arr / 2)
print(arr ** 2)

# Indexing and slicing
print(arr[0])
print(arr[1:3])
print(arr[-1])

# Reshaping arrays
arr = np.array([1, 2, 3, 4, 5, 6])
arr = arr.reshape(2, 3)
print(arr)

# Create a 2D NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# Matrix multiplication
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(np.dot(arr1, arr2))

# Statistical functions
arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))

# Random number generation
print(np.random.rand(3, 3))

# Linear algebra functions
arr = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(arr))
print(np.linalg.det(arr))

# Create a 3D NumPy array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)

# Advanced indexing
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[np.array([0, 1]), np.array([1, 2])])

# Broadcasting
arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[4], [5], [6]])
print(arr1 + arr2)

