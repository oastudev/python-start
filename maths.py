import math

#1 Calculate the radius of a circumference

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius

print(f"The Circumference is {round(circumference, 2)}cm")

#2 Calculate the area of a circle

radius = float(input('Enter the radius of a circle: '))

area = math.pi * pow(radius, 2)

print(f"The area is {round(area, 2)}cm^2")

#3 Calculate the hypotenuse of a right triangle

a = float(input("Enter  side A: "))
b = float(input("Enter  side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side c = {c}")

