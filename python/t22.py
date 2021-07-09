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
# Python - Access Dectionary Items
# 

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

# Example
# Get the value of the "model" key:

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x = thisdict["model"]
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

print(x)
# Mustang

# There is also a method called get() that will give you the same result:

# Example
# Get the value of the "model" key:

x = thisdict.get("model")
print(x)
# Mustang

#
# Get Keys
# The key() method will return a list all the keys in the dictionary.

# Example
# Get a list of the key:

x = thisdict.keys()
print(x)
# dict_keys(['brand', 'model', 'year'])

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

# Example
# Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x = car.keys()

print(x)    # before the change
# dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x)    # after the change
# dict_keys(['brand', 'model', 'year', 'color'])

#
# Get Values
#
# The value() method will return a list of all the values in the dictionary.

# Example
# Get a list of the values:

x = thisdict.values()
print(x)
# dict_values(['Ford', 'Mustang', 1964])

# The list of the value is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

# Example
# Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x = car.values()

print(x)    # before the change
# dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020

print(x)       # aafter the change
# dict_values(['Ford', 'Mustang', 2020])

# Example
# Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year" :1964
}

x = car.values()

print(x)    # before the change
# dict_values(['Ford', 'Mustang', 1964])

car["color"] = "red"

print(x)    # after the change
# dict_values(['Ford', 'Mustang', 1964, 'red'])

#
# Get Items
# The item() method will return each item in a dictionary, as tuples in a list.

# Example
# Get a list of the key:value pairs

x = thisdict.items()
print(x)
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# The returned list is a view of the items of the dictionart, meaning that any changes done to the dictionary will be reflected in the items list.

# Example
# Make a change in the original dictionary, and see that the items list gets updated as well:

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year" :1964
}
x = car.items()
print(x)        # before the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["year"] = 2020
print(x)        # after the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

# Example
# Add a new item to the original dictionart, and see that the items list gets updated as well:

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year" :1964
}
x = car.items()
print(x)    # before the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["color"] = "red"
print(x)    # after the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])

#
# Check if Key Exists
# To determine if a specified key is preent in a dictionary use the in keyword:

# Example
# Check if "model" is present in the dictionary:

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year" :1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# =======================================================================