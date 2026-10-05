import math # imports math functions and constants

# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x) - always rounds up to the nearest integer
# result = math.floor(x) - always rounds down to the nearest integer

# Circumference of a Circle
# radius = float(input("Enter the radius of a circle: "))
# circumfernce = 2 * math.pi * radius
# print(f"The circumference is {round(circumfernce, 2)}cm")

#Area of a Circle
# radius = float(input("Enter the radius of a circle: "))
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle is: {round(area, 2)} square inches")

#Calculate Hypotenuse (c) of a right triangle
sideA = float(input("Enter the length of side a: "))
sideB = float(input("Enter the length of side b: "))
hypotenuse = math.sqrt(pow(sideA, 2) + pow(sideB, 2))
print(f"The hypotenuse is: {round(hypotenuse, 2)}cm")




