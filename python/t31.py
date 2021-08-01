# Python Iterators
#

# Python Iterators
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically of the methods __iter__() and __next__() .

# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable Containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:

# Example
# Return an iterator from a tuple, and print each value:

mytuple = ("apple","banana","cherry")
myit = iter(mytuple)

print(next(myit))
# apple
print(next(myit))
# banana
print(next(myit))
# cherry

# Even strings are iterable pbjects, and can return an iterator:

# Example
# Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
# b
print(next(myit))
# a
print(next(myit))
# n
print(next(myit))
# a
print(next(myit))
# n
print(next(myit))
# a