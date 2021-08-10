##
## Python String islower() Method
##

# Example
# Check if all the character in the text are in lower case:

txt = "hello world"
x = txt.islower()
print(x)
# True

#
# Definition and Usage
#
# The islower() method returns True of all the characters are in lower case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.

#
# Syntax
# >> string.islower()

#
# Parameter Values
# No parameters.

#
# More Examples
#

# Example
# Check if all the characters in the texts are in lower case:

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
# False
print(b.islower())
# True
print(c.islower())
# False
