##
## Python -Modify Strings
##

# Python has a set of built-in methods that you can use on strings.

#
# Upper Case
#

# Example
# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
# HELLO, WORLD!

#
# Lower Case
#

# Example
# The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())
# hello, world!

#
# Remove Whitespace
#
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# Example
# The strip() method removes any whitespace from the begining or the end:

a = "Hello, World! "
print(a.strip())
# Hello, World!

#
# Replace String
#

# Example
# The replace() method replaces a string with another string():

a = "Hello, World!"
print(a.replace("H","J"))
# Jello, World!

#
# Split String
#
# The split() method returns a list where the text between the specified separator becomes the list items.

# Example
# The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(","))
# ['Hello', ' World!']

#
# String Methods
#
# Learn more about String Methods with our String Methods Reference