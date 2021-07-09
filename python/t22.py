#
# Python Dictionaries
#

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}

#
# Dictionary
#
# Dictionaries are used to store data calue values in key: value pairs.
# A dictionary is a collection which is ordered*, changeable and dose not allow duplicates.

## As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Dictionaries are writted with curly bracketsm and have keys and values:

# Example
# Create and print a dictionary:

thisdict = {
    "brand" :"Ford",
    "model" :"Mustang",
    "year"  :1964
}
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}

#
# Dictionary Items
# Dictionary items are ordered, changeable, and doesnot allow duplicates.
# Dictionary items are presented in ket:valuee pairs, and can be refered to by using the ley name.

# Example
# Print the "brand" value of the dictionary:

thisdict = {
    "brand" :"Ford",
    "model" :"Mustang",
    "year"  :1964
}
print(thisdict["brand"])
# Ford

#
# Ordered or Unordered?

## As Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

#
# Changeable
# Dictionaries are changeable, meaning that er can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
# Dictionaries cannot have items with the same key:

# Example
# Duplicate values will overwrite existing values:

thisdict = {
    "brand" :"Ford",
    "model" :"Mustang",
    "year"  :1964,
    "year"  :2020
}
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#
# Dictionary Length
#
# To determine how many items a dictionary has, use the len() function:

# Example
# Print the number of items in the dictionary:
print(len(thisdict))
# 3

# Dictionary Items- Data Types
# The values in dictionary items can be of any data type:

# Example
# String, int, boolean, and list data types:

thisdict = {
    "brand"     :"Ford",
    "electric"  :False,
    "year"      :1964,
    "colors"    :["red","white","blue"]
}
print(thisdict)
# {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

# type()
# From Python's perspective, dictionaries are defined as objects with the data type 'dict':
# <class 'dict'>

# Example
# Print the data type of a dictionary:

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(type(thisdict))
# <class 'dict'>

#
# Python Collections(Arrays)
# There are four collection data types in the Python programming language:
# - List is a collection which is ordered and changeable. Allows duplicate members.
# - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# - Set is a collection which is unordered and unindexed. No duplicate members.
# - Ditionary is a collection which is ordered and changeable. No dupliicate members.

# When choosing a collection type, it is useful to understand the properties of that type.
# Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficienct or security.

# ====================================================================================

#
# Python
# 