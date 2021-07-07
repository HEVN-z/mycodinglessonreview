#
# Python Lists
#

mylist = ["apple","banana","cherry"]

# List
# List are used to store multiple items in a single variable.
# Liist are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set and Dictionary, all with different qualities and usage.
# List are create using square brackets:

# Example
# Create a List:

thislist = ["apple", "banana","cherry"]
print(thislist)

# List Items
# List items are ordered, changeable, and allow duplicate value.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in list after it has been created.

# Allow Duplicates
# Sinc lists are indexed, Lists can have items with the same value:

# Example
# List allow duplicate value:

thislist = ["apple","banana","cherry","apple","cherry"]
print(thislist)

#
# List Leigth
#
# To determine how many items a list has, use the len() function:

# Example
# Print the number if items in the list:

thislist = ["apple","banana","cherry"]
print(thislist[1]) # banana
print(len(thislist)) # 3
print(thislist[len(thislist)-1]) # cherry

#
# List Items - Data Types
#
# Example
# String, int and boolean data types:

list1 = ["apple","banana","cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# A list can contain different data types:

# Example
# A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]

print(list1)

#
# type()
# 
# From Python's perspective, lists are defined as objects with data type 'list':

# <class 'list'>

# Example
# What is the data type of a list?

mylist = ["apple","banana","cherry"]
print(type(mylist))

