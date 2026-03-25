age = 24
if age >= 18:
    print("your are adult")
else:
    print("you are not adult")

marks = 85

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("fail")


x = 10
y = 20

print( x > y)
print( x < y)
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)

speed = 12
battery = 40

if speed > 10 and battery > 20:
    print("Robot can run fast")
elif speed > 10 or battery <= 20:
    print("Robot can run slow")
else:
    print("Normal mode")

distance = 0.6

if distance > 0.5:
    print("Stop Obstacle very close!")
elif distance < 1.0:
    print("Slow Down")
else:
    print("Move Forward")


battery = 35
temp = 47

if battery < 20:
    status = "Low Battery"
elif temp > 60:
    status = "Overheating"
elif 20 <= battery <= 80:
    status = "Good"
else:
    status = "Fully charged"

print("Robot Status ->", status)