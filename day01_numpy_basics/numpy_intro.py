import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("Array: ", arr)
print("Shape: ", arr.shape)
print("Type: ", arr.dtype)

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("\nMatrix:\n", matrix)
print("Shape: ", matrix.shape)

print("\nAdd 5: ", arr + 5)
print("Multiply by 2: ", arr * 2)

print("\nSum bu axis 0: ", matrix.sum(axis=0))
print("Sum by axis 1:", matrix.sum(axis=1))

data = np.array([[2, 4, 6],
                 [8, 10, 12],
                 [14, 16, 18]])

norm = (data -data.min()) / (data.max() - data.min())
print("\nNormalized data:\n", norm)