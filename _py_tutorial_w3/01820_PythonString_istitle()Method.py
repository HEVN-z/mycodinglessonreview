##
## Python String istitle() Method
##

# Example
# Check if each word start with an upper case letter:

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
# True

#
# Definition and Usage
#
# The isititle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
# Symbols and numbers are ignored.

#
# Syntax
# >> string.istitle()

# Parameter Values
# No parameters.

#
# More Examples
#

# Example
# Check if each word start with an upper case letter:

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
print(a.istitle())
# False
print(b.istitle())
# True
print(c.istitle())
# True
print(d.istitle())
# True

