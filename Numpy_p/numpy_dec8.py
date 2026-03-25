import numpy as np
arr = np.arange(12)
print(arr.reshape(3, 4))

arr = np.array([1, 2, 3])
print(arr + 10)
print(arr * 5)

arr = np.array([10, 5, 30, 2, 50])
print(arr[arr > 10])

mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.sum(mat, axis=0))
print(np.sum(mat, axis=1))
print(np.random.rand(3))
print(np.random.randint(1, 10, 5))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.vstack((a, b)))
print(np.hstack((a, b)))