import numpy as np
print("==== Robot Sensor Brain v1 ====")

distances = np.array([1.8, 1.2, 0.9, 0.6, 2.0])
print("\nDisatance readings (m) ->", distances)

print("\nNumber of readings ->", len(distances))
print("Closet obstacle ->", np.min(distances), "m")
print("Farthest obstacle ->", np.max(distances), "m")
print("Average distance ->", np.mean(distances), "m")

actions = []

for d in distances:
    if d < 0.7:
        actions.append("STOP")
    elif d < 1.0:
        actions.append("SLOW")
    else:
        actions.append("Walk")

print("\nActions for each reading->", actions)

need_stop = np.any(distances < 0.7)
need_slow = np.any((distances >= 0.7) & (distances < 1.0))

print("\n==== Summary Decision ====")
if need_stop:
    print("Danger close! Robot should stop!")
elif need_slow:
    print("Some obstacles nearby. Robot should slow down!")
else:
    print("No obstacles nearby. Robot can walk!")   