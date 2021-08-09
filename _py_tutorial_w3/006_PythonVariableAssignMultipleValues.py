##
## Python Variables - Assign Multiple Values
##

#
# Many Values to Multiple Variables
#
# Python allows you to assign value to multiple variables in one line:

# Example

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Orange
# Banana
# Cherry

#
# One Value to Multiple Variables
#
# And you can assign the same value to multiple variables in one line:

# Example

x = y = z = "Orange"
print(x)
print(y)
print(z)
# Orange
# Orange
# Orange

#
# Unpack a Collection
#
# If you have a collection of values in a list, tuple etc.
# Python allows you extract the values into variables. This is called unpacking.

# Example

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# apple
# banana
# cherry