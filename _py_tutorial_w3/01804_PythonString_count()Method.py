##
## Python String count() Method
##

# Example
# Return the number of times the value "apple" appears in the string:

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
# 2

#
# Definition and Usage
#
# The count() method returns the number of times a specified value appears in the string.

#
# Syntax
# >> string.count(value, start, end)

#
# Parameter Value

# Parameter                 Description
# Value                     Required. A String. The string to value to search for
# start                     Optional. An Integer. The opsition to start the search. Default is 0
# end                       Optional. An integer. The position to end the search. Default is the end of the string

#
# More Examples
#

# Example
# Search from position 10 to 24:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)
# 1
