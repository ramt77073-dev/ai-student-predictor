n = 17
def EvenOdd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

EvenOdd(n)

age = 14
if age >= 18:
    print("Adult")
elif age < 18:
    print("Minor")
else:
    print("Invalid age")

speed = 72

if speed > 80:
    print("Over speed")
elif 60 <= speed <= 80:
    print("Normal speed")
else:
    print("Low speed")

battery = 18
if battery < 20:
    print("Low battery")
elif 20 <= battery <= 80:
    print("Normal battery")
else:
    print("High battery")

distance = 0.4
if distance < 0.5:
    print("Stop")
elif 0.5 <= distance <= 1:
    print("Slow down")
elif 1 < distance <= 2:
    print("Normal speed")
else:
    print("High speed")
    

temp = 10
if temp < 10:
    print("Cold")
elif 10 <= temp <= 30:
    print("Normal")
else:
    print("Hot")
    
age = 65
if age < 18:
    print("50 percent Discount")
elif 18 <= age <= 60:
    print("10 percent Discount")
else:
    print("30 percent Discount")

password = "1234"
if password == "1234":
    print("Login successful")
else:
    print("Login failed")

n = -20
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

battery = 70
temperature = 55
if battery > 20 and temperature < 60:
    print("Healthy")
else:
    print("Unhealthy")