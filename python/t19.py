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

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

# Example
# Using the list() constructor to make a list:

thislist = list(("apple","banana","cherry")) # note the double round-brackets
print(thislist)

# ===========================================================================

#
# Python Collections(Arrays)
# 
# There are four collection data types in the Python programming language:
# - List is a collection which is ordered and changeable. Allows duplicate members.
# - Tuple is collection which is ordered and unchangeable. Allow duplicate members.
# - Set is a collection which is unordered and unindeced. No duplicate members.
# - Dictionary is a collection which ordered* and changeable. No duplicate members.

# *As of Python version 3.7, dictionaries are ordered, In Python 3.6 and earlier, dictionariese are unordered.

# When choosing a collection type, it is useful to understand the properties of that type.
# Choosing the right type fir a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

#
# Python - Access List Items
#

# Access Items
# List items are indexed and you can access them by referring to the index number:

# Example
# Print the second item of the list:
thislist = ["apple","banana","cherry"]
print(thislist[1]) # banana

# NOTE: The first item has indes 0.

#
# Negative Indexing
#
# Negative indexing means start from the end

# -1 refer to the last item, -2 refer ti the second last item etc.

# Example
# Print the last item of the list:

thislist = ["apple","banana","cherry"]
print(thislist[-1]) # cherry

# 
# Range of Indexes
#
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.

# Example
# Return the third, fourth, and fifth item:

thislist = ["apple","banana","cherry","kiwi","melon","mango"]
print(thislist[0:6]) # ['apple', 'banana', 'cherry', 'kiwi', 'melon', 'mango']
print(thislist[1:5]) # ['banana', 'cherry', 'kiwi', 'melon']
print(thislist[2:4]) # ['cherry', 'kiwi']
print(thislist[2:5]) # ['cherry', 'kiwi', 'melon']

## NOTE: The search will start at index 2(included) and end at index 5 (not included).
## Remember that the first item has index 0.

# By leaving out the start value, the range will start the first item:

# Example
# This example returns the item from the begining to, but NOT including, "kiwi":

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[:4]) # ['apple', 'banana', 'cherry', 'orange']

# By leaving out the end value, the range will go on to the end of list:

# Example
# This example returns the item from "cherry" to the end:

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:]) # ['cherry', 'orange', 'kiwi', 'melon', 'mango']

#
# Range of Negative Indexed
#
# Specify negative indexes if you want to start the search from the end of the list:

# Example
# This example returns the item from "orange"(-4) to , but NOT including "mango"(-1):

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[-4:-1]) # ['orange', 'kiwi', 'melon']

#
# Check if Item Exists
#
# To determine if a specified item is present in a list use the in keyword:

# Example
# Check if "apple" is present in the list:

thislist = ["apple","banana","cherry"]
if "apple" in thislist:
    print("Yes, 'apple is in the fruits list") 

# Yes, 'apple is in the fruits list

# ============================================================================

#
# Python - Change List Items
#

# Change Item Lalue
# To change the value of a specific item, refer to the index number:

# Example
# Change the second item:

thislist = ["apple","banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# ['apple', 'blackcurrant', 'cherry']

#
# Change a Range of Item Values
#
# To change the value of items within a specific, range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

# Example
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple","banana","cherry","orange","kiwi","mango"]
thislist[1:3] = ["blackcurrant","watermelon"]
print(thislist)

# ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# If you insert more items than you replace, the new items will be insert where you specified, and the remaining items will move accordingly:

# Example
# Change the second value by replacing it with two new values:

thislist = ["apple","banana","cherry"]
thislist[1:2] = ["blackcurrant","watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'cherry']

## NOTE: The length of the list will change when the number of items inserted does not match the number of items replaced.

# If you insert less items that you replaace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# Example
# Change the second and third value by replacing it with one value:

thislist = ["apple","banana","cherry","strawberry","orange"]
thislist[1:3] = ["watermelon"]
print(thislist)

# ['apple', 'watermelon', 'strawberry', 'orange']

#
# Insert Items
#
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:

# Example
# Insert "watermelon" as the third item:

thislist = ["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)

# ['apple', 'banana', 'watermelon', 'cherry']

## NOTE: As a result of the example above, the list will now contain 4 items.

# =============================================================================

#
# Python - Add List Items
#
# Append Items
# To add an item to the end of the list, use the append() method:

# Example
# Using the append() method to append an item:

thislist = ["apple","banana","cherry"]
thislist.append("orange")
print(thislist)

# ['apple', 'banana', 'cherry', 'orange']

# Insert Items
# To insert a list item at a specified index, use the insert() method.
# The insert() method insert an item at the specified index:

# Example
# Insert an item as the second position:
thislist = ["apple","banana", "cherry"]
thislist.insert(1,"orange")
print(thislist)

# ['apple', 'orange', 'banana', 'cherry']

## NOTE: As a result of the examples above, the list will now contain 4 iitems.

#
# Extend List
#
# To append elements from another list to the current list, using the extend() method.

# Example
# Add the elements of tropical to thislist:

thislist = ["apple","banana","cherry"]
tropical = ["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)

# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# The element will be added to the end of the list

#
# Add Any Interble
#
# The extend() method does not have to append lists, you can add any interable object(tuples,sets,dictionaries etc.)

# Example
# Add elements of a tuple to a list:

thislist = ["apple","banana","cherry"]
thistuple = ("kiwi","orange")
thislist.extend(thistuple)
print(thislist)

# ['apple', 'banana', 'cherry', 'kiwi', 'orange']

# ===============================================================================

#
# Python - Remove List Items
#
# Remove Specified Item
# The remove() method removes the specified item.

# Example
# Remove "banana"

thislist = ["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)

# ['apple', 'cherry']

# 
# Remove Specified Index
#
# Example
# Remove the second item:

thislist = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

# ['apple', 'cherry']

# If you do not specify the index, the pop() method remove the last item.

# Example
# Remove the last item:

thislist = ["apple","banana","cherry"]
thislist.pop()
print(thislist)

# ['apple', 'banana']

# The del keyword also removes the specified indes:

# Example 
# Remove the first item:

thislist = ["apple","banana","cherry"]
del thislist[0]
print(thislist)

# ['banana', 'cherry']

# The del keyword can also delete the list completely.

# Example
# Delete the entire list:

thislist = ["apple","banana","cherry"]
del thislist
# print(thislist)

# NameError: name 'thislist' is not defined

#
# Clear the List
#
# The clear() method empties the list.
# The list still remains, but it has no content.

# Example
# Clear the list content:

thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)

# []

# =============================================================================

#
# Python - Loop Lists
#

# Loop Through a List
# You can loop through the list items by using a for loop:

# Example
# Print all items in the list, one by one

thislist = ["apple","banana","cherry"]
for x in thislist:
    print(x)

# apple
# banana
# cherry

# Learn more about for loops in our Python For Loops Chapter:

#
# Loop Through the Index Numbers
#
# You can also loop through the list items by refering to their index number.
# Use the range() and len() functions to create a suitabke iterable.

# Example
# Print all items by referring to their index number:

thislist = ["apple","banana","cherry"]
for i in range(len(thislist)):
    print(thislist[i])

print(range(3))
print(range(2,3))
# apple
# banana
# cherry
# range(0, 3)
# range(2, 3)

# The iterable created in the example above is [0, 1, 2].
