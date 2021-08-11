##
## Python - Add List Items
##

#
# Append Items
#
# OTo add an item to end of the list, use the append() method:

# Example
# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# ['apple', 'banana', 'cherry', 'orange']

#
# Insert Items
#
# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at specified index:

# Examplpe
# Insert an item as the second position:

thislist = ["apple","banana","cherry"]
thislist.insert(1,"orange")
print(thislist)
# ['apple', 'orange', 'banana', 'cherry']

# NOTE: As a result the examples above, the lists will now contain 4 items.

# 
# Extend List
#
# To append elements from another list to the current list, use the extend() method.

#
# Example
#
# Add the element of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# The elements will be added to the end of the list.

#
# Add Any Iterable
#
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionary etc.)

# Example
# Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
# ['apple', 'banana', 'cherry', 'kiwi', 'orange']

