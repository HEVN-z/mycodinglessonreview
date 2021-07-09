#
# Python - Sets
#

myset = {"apple","banana","cherry"}

#
# Set
#
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with qualities and usage.
# A set is a collection which is both unordered and unindexed.
# Sets are written with curly brackets.

# Example
# Create a Set:

thisset = {"apple","banana","cherry"}
print(thisset)
# {'cherry', 'apple', 'banana'}

## NOTE: Sets are unordered, so you cannot be sure in which order the items will appear.

#
# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.

## Once a set is created, you cannot change its items, but you can add new items.

# Duplicates Not Allowed
# Sets cannot have two items with the same value.

# Example
# Duplicate value will bee ignored:

thisset = {"apple","banana","cherry","apple"}
print(thisset)
# {'banana', 'apple', 'cherry'}

#
# Get the Length of a Set
# To determine how many items a set has, use the len() method.

# Example
# Get the number of items in a set:

thisset = {"apple","banana","cherry"}
print(len(thisset))
# 3

# Set Items - Data Types
# Set items can be of any data type:

# Example
# String, int and boolean data types:

set1 = {"apple","banana","cherry"}
set2 = {1,5,7,9,3}
set3 = {True,False,False}

# A set can contain different data type:

# Example
# A set with strings, integers and boolean values:

set1 = {"abc",34,True,40,"male"}

#
# type()
# From Python's perspective, set are defined as objects with the data type 'set':
# <class 'set'>

# Example
# What is the data type of a set?

myset = {"apple","banana","cherry"}
print(type(myset))
# <class 'set'>

# The set() Constructor
# It is also possible to use the set() constructor to make a set.

# Example
# Using the set() constructor to make a set:

thisset = set(("apple","banana","cherry")) # note the double round-brackets
print(thisset)
# {'cherry', 'banana', 'apple'}

# Python Collections(Arrays)
# There are four collection data types in the Python programming language:
# - List is a collection which is ordered and changeable. Allows duplicate members.
# - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# - Set is a collection which is unordered and unindexes. No duplicate members.
# - Dictionary is a collection which is ordered* and changeable. No duplicate members.

# *As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# When choosing a collection type, it iis useful to understand the properties of that type.
# Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

# =============================================================================

#
# Python - Access Set Items
#
# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the sset items using a for loop, or ask if a sprcified value is present in a set, by using the in keyword.

# Example
# Loop through the set, and printable the values:

thisset = {"apple","banana","cherry"}
for x in thisset:
    print(x)
# apple
# banana
# cherry

# Example
# Check if "banana" is present in the set:

thisset = {"apple","banana","cherry"}
print("banana" in thisset)
# True

#
# Change Items
#
## Once a set is created, you cannot change its items, but you can add new items.

# ==========================================================================

#
# Python - Add Set Items
#

# Add Items
## Once a set is created, you cannot change its items, but you can add items.

# To add one item to a set use the add() method.

# Example
# Add an item to a set, using the add() method:

thisset = {"apple","banana","cherry"}
thisset.add("orange")
print(thisset)
# {'cherry', 'apple', 'orange', 'banana'}

