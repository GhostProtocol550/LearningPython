# Thanks to Bro Code on Youtube for the python tutorials
# typecasting = the process of converting a value of one data type to another
# (string, integer, float, boolean)
# Explicit vs Implicit

name = "Daniel" # string
age = 21 # integer
gpa = 3.8 # float
isStudent = True # boolean

# Explicit typecasting - manually converting data types
# print(type(age)) type() gives you the type of variable
# age = float(age)
# print(type(age)) turns age from an iteger to a float
# name = bool(name)
# print(name)

# Implicit typecasting - automatically converting data types
x = 2
y = 2.0
x = x / y
print(x)