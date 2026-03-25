import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [35, 45, 55, 65, 75, 85]

plt.scatter(hours, marks, color="red")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Student Data")
plt.show()