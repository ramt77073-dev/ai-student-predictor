import numpy as np
print("===== ROBOT BRAIN v3 ======")

angles_deg = np.array([30, 45, 60])
angles_rad = np.radians(angles_deg)
torque = angles_rad * 0.5
total_torque = np.sum(torque)
movement_vrctor = np.array([1.5, 3.0, 4.5])

distances = np.array([1.8, 1.2, 0.9, 0.6, 2.0])

actions = []

for d in distances:
    if d < 0.7:
        actions.append("stop")
    elif d < 1.0:
        actions.append("slow down")
    else:
        actions.append("move forward")

closest = np.min(distances)

battery_level = 32

if battery_level > 70:
    battery_status = "FULL"
elif battery_level > 40:
    battery_level = "NOrmal"
elif battery_level > 20:
    battery_status = "LOW"
else:
    battery_status = "CRITICAL"

if "STOP" in actions or closest < 0.7:
    speed = 0
elif "SLOW DOWN" in actions or battery_level < 20:
    speed = 1.0
else:
    speed = 2.0

tilt_angle = 18

if tilt_angle > 30:
    fall_status = "Fall Detected ! Robot stopping!"
    speed = 0
else:
    fall_status = "stable"

print("===== STATUS REPORT ======")
print(f"Total torque-> {round(total_torque, 3)} Nm")
print(f"Movement vector-> {movement_vrctor}")
print(f"Closest Obstacle-> {closest} m")
print(f"sensor Actions-> {actions}")
print(f"battery level-> {battery_level}%  -> {battery_status}")
print(f"Robot Speed -> {speed} m/s")
print(f"Tilt Angle -> {tilt_angle} -> {fall_status}")
print("==========================================\n")
