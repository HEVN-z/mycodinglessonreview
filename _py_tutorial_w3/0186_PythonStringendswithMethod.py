##
## Python String endswith() Method
##

# Example
# Check if the string ends with a punctuation sign(.):

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
# True

#
# Definition and Usage
#
# The endswith() method returns True if the string ends with the specified value, otherwise False.

#
# Syntax
# >> string.endswith(value, start, end)

#
# Parameter Values
# Parameter             Description
# value                 Requited. The value to check if the string ends with
# start                 Optional. An Integer specifying at which position to start the search
# end                   Optional. An Integer specifying at which position to end the search

#
# More Examples
#

# Example
# Check if the string ends with the phrase "my world.":

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)
# True

# Example
# Check if position 5 to 11 ends with the phrase "my world."

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)
# False

