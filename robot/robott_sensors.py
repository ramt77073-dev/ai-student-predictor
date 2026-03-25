import numpy as np
print("===== ROBOT SENSORS BRAIN v1 =====")

distances = np.array([1.8, 1.2, 0.9, 0.6, 2.0])
print("\nDistance readings(m) ->", distances)
print("\nNumber of readings ->", len(distances))
print("Closest obstacle ->", np.min(distances))
print("Furthest obstacle ->", np.max(distances))
print("Average distance ->", np.mean(distances))

actions = []
for d in distances:
    if d <= 0.7:
        actions.append("STOP")
    elif d <= 1.5:
        actions.append("SLOW DOWN")
    else:
        actions.append("MOVE FORWARD")

print("\nActions for each reading ->", actions)

print("\n==== Summary Decision =====")
if np.min(distances) <= 0.7:
    print("Danger close! Robot should Stop!")
else:
    print("Safe to walk.")