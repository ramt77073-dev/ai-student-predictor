import numpy as np
print("===== ROBOT BRAIN v2 -:EG + SENSORS =====\n")
angles_deg = np.array([30, 45, 60])
print("Joint Angles(deg)", angles_deg)

angles_rad = np.radians(angles_deg)
print("Joint Angles(rad)->", angles_rad)

torque = angles_rad * 0.5
print("Torque->", np.round(torque, 3))

total_torque = np.sum(torque)
print("Total Torque->", round(total_torque, 3))

movement_vector = np.array([1.5, 3.0, 4.5])
print("Movement Vector->", movement_vector, "\n")

distances = np.array([1.8, 1.2, 0.9, 0.6, 2.0])
print("distance readings(m)->", distances)

num_readings = len(distances)
closest = np.min(distances)
farthest = np.max(distances)
avg_distance = np.mean(distances)

print("Number of readings->", num_readings)
print("Closest distance->", closest, "m")
print("Farthest distance->", farthest, "m")
print("Average distance->", round(avg_distance, 2), "m\n")

actions = []

for d in distances:
    if d < 0.7:
        actions.append("STOP")
    elif d < 1.0:
        actions.append("SLOW DOWN")
    else:
        actions.append("MOVE FORWARD")

print("Actions for each readings->", actions)

print("\n===== Summary Decision =====")
if closest < 0.7:
    print("DAnger close! Robot Stop!")
elif avg_distance < 1.0:
    print("Danger! Slow Down!")
else:
    print("Path is clear, robot can move.")

print("\n===== STATUS REPORT =====")
print(f"Total Torque: {round(total_torque, 3)}")
print(f"Average distance: {round(avg_distance, 2)} m")
print(f"Leg movement vector: {movement_vector}")
print(f"Sensor Action: {actions}")
