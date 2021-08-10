##
## Python String format() Method
##

# Example
# Insert the price inside the placeholder, the price shoulder be fixed point, two decimal format:

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
# For only 49.00 dollars!

#
# Definition and Usage
#
# The format() method formats the specified value(s) and insert them inside the string's placeholder section below.
# The format() method returns the formatted string.

#
# Syntax
# >> string.format(value1, value2...)

# Parameter Values
# Parameter             Description
# value1                Required. One or more values that
# value2...             should be formatted and inserted in the string.
#                       The values are either a list of values separated by commas, a key=value list, or a combination of both.
#                       The value can be of any data type.

#
# The Placeholders
#
# The placeholders can be identified using named indexes {price}, numbered indexes {0}, or empty placeholders {}.

# Example
# Using different placeholder values:

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

#
# Formattinig Types
#
# Inside the placeholders you can add a formatting type to format the result:
#   :<  Left aligns the result (within the available space)
#   :>  Right aligns the result (within the available space)
#   :^  Center aligns the result (within the available space)
#   :=  Place the sign to the left most position
#   :+  Use a plus sign to indicate if the result is positive or negative
#   :-  Use a minus sign for negative values only
#   :   Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
#   :,  Use a comma as a thousand separator
#   :_  Use a underscore as a thousand separator
#   :b  Binary format
#   :c  Converts the value into the corresponding unicode character
#   :d  Decimal format
#   :e  Scientific format, with a lower case e
#   :E  Scientific format, with an upper case E
#   :f  Fix point number format
#   :F  Fix point number format, in uppercase format (show inf and nan as INF and NAN)
#   :g  General format
#   :G  General format (using a using a upper case E for scientific notations)
#   :o  Octal format
#   :x  Hex format, upper case
#   :X  Hex format, upper case
#   :n  Number format
#   :%  Percentage format
