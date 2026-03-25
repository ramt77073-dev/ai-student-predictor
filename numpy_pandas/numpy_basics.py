import numpy as np

print("=== NUMPY BASICS FOR ML ===\n")


arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Type:", type(arr))
print("Shape:", arr.shape, "\n")


data = np.array([
    [1.5, 2.3, 3.1],
    [4.0, 5.2, 6.3],
    [7.1, 8.4, 9.0]
])
print("Data:\n", data)
print("Shape:", data.shape)
print("Rows:", data.shape[0], "Cols:", data.shape[1], "\n")


print("Mean of arr:", np.mean(arr))
print("Sum of arr:", np.sum(arr))
print("Max of arr:", np.max(arr))
print("Min of arr:", np.min(arr), "\n")


arr2 = np.array([10, 20, 30, 40, 50])
print("arr :", arr)
print("arr2:", arr2)
print("arr + arr2:", arr + arr2)
print("arr * 2:", arr * 2, "\n")


print("First 3 elements of arr:", arr[:3])
print("First 2 rows of data:\n", data[:2])
print("Second column of data:", data[:, 1], "\n")
