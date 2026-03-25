import numpy as np

print("==== ROBOT LEG MATH v1 ====")

angles = np.array([30, 45, 60])
print("\nJoint Angles (degrees)->", angles)

radians = np.radians(angles)
print("\nJoint Angles (radians)->", radians)

torque = radians * 0.5
print("Torque at each joints->", torque)

total_torque = np.sum(torque)
print("Total Torque->", total_torque)

movement = np.array([1.5, 3.0, 4.5])
print("\nScaled Movement Vector->", movement)