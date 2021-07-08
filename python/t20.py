#
# Python Tuples
#

mytuple = ("apple", "banana", "cherry")

#
# Tuple
#
# Tuple are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionart, all with different qualities and usage.
# A tuple is collection which is ordered and unchangeable.
# Tuple are written with round brackets.

# Example
# Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)
# ('apple', 'banana', 'cherry')

#
# Tuple Items
#
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index[0], the second item has index[1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Sinc tuples are indexed, they can have items with the same value:

# Example
# Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# ('apple', 'banana', 'cherry', 'apple', 'cherry')

#
# Tuple Length
# To determine how many items a tuple has, use the len() function:

# Example
# Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
# 3

#
# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# Example
# One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))
# <class 'tuple'>

thistuple = ("apple")
print(type(thistuple))
# <class 'str'>

#
# Tuple Items - Data Types
# Tuple items can be of any data type:

# Example
# String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
print(tuple1)           # ('apple', 'banana', 'cherry')

tuple2 = (1, 5, 7, 9, 3)
print(tuple2)           # (1, 5, 7, 9, 3)

tuple3 = (True, False, False)
print(tuple3)           # (True, False, False)

# A tuple can contain different data types:

# Example
# A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")

#
# type()
#
# From Python's perspective, tuples are defined as objects with the data type 'tuple':
# <class 'tuple>

# Example
# What is the data type of a tuple?

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
# <class 'tuple'>

#
# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

# Example
# Using the tuple() method to make a tuple:

thistuple = tuple(("apple","banana","cherry")) #NOTE the double round-brackets
print(thistuple)
# ('apple', 'banana', 'cherry')

#
# Python Collections(Arrays)
#
# There are four collection data types in the Python programming language:
# - List is a collection which is ordered and changeable. Allows duplicate members.
# - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# - Set is a collection which is unordered and unindexed. No duplicate members.
# - Dictionary is a collection which ordered* and changeable. No duplicate members.

## * As of Python version 3.7, dictionaries are ordered, In Python 3.6 and earlier, dictionaries are unordered.

# When choosing a collection type, it is useful to understand the properties of that type.
# Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

# ==============================================================================

#
# Python - Access Tuple Items
#

# Accesss Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:

# Example
# Print the second item in the tuple:

thistuple = ("apple","banana","cherry")
print(thistuple[1])
# banana

## NOTE The first item has index 0.

#
# Negative Indexing
#
# Negative indexing means start from the end.
# -1 refers to the last item
# -2 refers to the second last item etc.

# Example
# Print the last item of the tuple:

thistuple = ("apple","banana","cherry")
print(thistuple[-1])
# cherry

#
# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When can specifying a range, the return value will be a new tuple with the specified items.

# Example
# Return the third, fourth, and fifth item:

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:5])
# ('cherry', 'orange', 'kiwi')

## NOTE: The search will start at index 2 (included) and end at index 5 (not included).

## Remember that the first item has index 0.

# By leaving out the start value, the range will start at the first item:

# Example
# This example returns the items from the begining to, but NOT included, "kiwi":

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[:4])
# ('apple', 'banana', 'cherry', 'orange')

# By leaving out the end value,the range will go on to the end of the list:

# Example
# This example returns the items from "cherry" and to the end:

thistuple = ("apple","banana","cherry","orange","kiwi","malon","mango")
print(thistuple[2:])
# ('cherry', 'orange', 'kiwi', 'malon', 'mango')

#
# Range of Negative Indexes
#
# Specify negative indexes if you want to start the search from the end of the tuple:

# Example
# This example returns the items from index -4 (included) to index -1 (excluded)

thistuple = ("apple","banana","cherry","orange","kwii","melon","mango")
print(thistuple[-4:-1])
# ('orange', 'kwii', 'melon')

#
# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:

# Example
# Check if "apple" is present in the tuple:

thistuple = ("apple","banana","cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

#
# ===========================================================================

#
# 
#