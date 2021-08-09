##
## Python - Format - Strings
##

#
# String Format
#
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

# Example
# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

# Example
# Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# My name is John, and I am 36

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

# Example

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} places of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# I want 3 places of item 567 for 49.95 dollars.

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

# Example

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))
# I want to pay 49.95 dollars for 3 pieces of item 567.

