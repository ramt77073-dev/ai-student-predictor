battery = 65
speed = 40
distance = 0.7
temperature = 38
tilt_angle = 12

if battery < 20:
    battery_status = "Low"
elif 20 <= battery <= 80:
    battery_status = "Medium"
else:
    battery_status = "High"

if speed > 80:
    speed_status = "Fast"
elif 40 <= speed <= 80:
    speed_status = "Medium"
else:
    speed_status = "Slow"

if distance < 0.5:
    distance_action = "Stop - Obstacle very close!"
elif 0.5 <= distance <= 1:
    distance_action = "Slow down- Obstacle  a head!"
else:
    distance_action = "Safe"

if temperature < 20:
    temp_status = "Clod"
elif 20 <= temperature <= 40:
    temp_status = "Normal"
else:
    temp_status = "Hot"

if tilt_angle > 30:
    fall_status = "Fall detected - Robot stopping!"
else:
    fall_status = "Stable"

if fall_status.startswith("FALL"):
    final_action = "Stop Immediately"
elif battery_status == "Low":
    final_action = "Return to charging station"
elif "STOP" in distance_action:
    final_action = "Stop and wait"
elif temp_status.startswith("HOt"):
    final_action = "Reduce speed"
else:
    final_action = "Move safe"

print("\n========= Robot Satus report =====")
print("Battery status:", battery_status)
print("Speed status:", speed_status)
print("Distance status:", distance_action)
print("Temperature status:", temp_status)
print("Tilt Angle:", tilt_angle, "=>", fall_status)
print("-"*50)
print("Final Action:", final_action)
print("="*50)