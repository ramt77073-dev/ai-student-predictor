import numpy as np
print("==== ROBOT LEG MATH ====")

angles = np.array([30, 45, 60])
print("Joint Angles (degrees):", angles)

radians = np.radians(angles)
print("Joint Angles (radians):", radians)

torque = radians * 0.5
print("Torque at each joints:", torque)

total_torque = np.sum(torque)
print("Total Torque:", total_torque)

movement_vector = np.array([1, 2, 3])
scaled = movement_vector * 1.5
print("Scaled Movement Vector:", scaled)

print("==== ROBOT LEG MATH ====")