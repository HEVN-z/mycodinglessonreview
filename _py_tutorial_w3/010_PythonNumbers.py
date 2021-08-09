##
## Python Numbers
##

#
# Python Numbers
#
# There are three numeric types in Python:
#   ◼ int
#   ◼ float
#   ◼ complex
# Variables of numeric types are created when you assign a value to them:

# Example

x = 1   # int
y = 2.8 # float
z = 1j  # complex

# To verify the type of any object in Python, use the type() function:

# Example

print(type(x))
# <class 'int'>
print(type(y))
# <class 'float'>
print(type(z))
# <class 'complex'>

#
# Int
#
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited lengthh.

# Example
# Integers:

x = 1
y = 35656222554887711
z = -3255522
print(type(x))
# <class 'int'>
print(type(y))
# <class 'int'>
print(type(z))
# <class 'int'>

#
# Float
#
# Float, or "floating point number" is a number, positive oor negative, containing one or more decimals.

# Example
# Floats:

x = 1.10
y = 1.0
z = -35.59
print(type(x))
# <class 'float'>
print(type(y))
# <class 'float'>
print(type(z))
# <class 'float'>

# Float can also be scientific numbers with an "e" to indicate the power of 10

# Example
# Floats:

x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
# <class 'float'>
print(type(y))
# <class 'float'>
print(type(z))
# <class 'float'>

#
# Complex
#
# Complex numbers are written with a "j" as the imaginary part:

# Example
# Complex:

x = 3+5j
y = 5j
z = -5j
print(type(x))
# <class 'complex'>
print(type(y))
# <class 'complex'>
print(type(z))
# <class 'complex'>

#
# Type Conversion
#
# You can convert from one type to another with the int(), float(), and complex() methods:

# Example
# Convert from one tyoe to another:

x = 1       # int
y = 2.8     # float
z = 1j      # complex
#Convert from int to float:
a = float(x)
#Convert from float to int:
b = int(y)
#Convert from int to complex:
c = complex(x)
print(a)
# 1.0
print(b)
# 2
print(c)
# (1+0j)
print(type(a))
# <class 'float'>
print(type(b))
# <class 'int'>
print(type(c))
# <class 'complex'>

#
# Random Number
#
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

# Example
# Import the random module, and display a random number between 1 and 9:

import random
print(random.randrange(1, 10))
# 5