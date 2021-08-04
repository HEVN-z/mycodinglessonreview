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

# Loop Through an Iterator
#
# We can also use a for loop to iterate through an iterable an iterable object:

# Example
# Iterate the value of a tuple:

mytuple = ("apple","banana","cherry")
for x in mytuple:
    print(x)
# apple
# banana
# cherry

# Example
# Iterate the character of string:

mystr = "banana"

for x in mystr:
    print(x)
# b
# a
# n
# a
# n
# a

# The for loop actually creates an iterator object and executes the next() method for each loop.

#
# Create an Iterator
#
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have to function called __init__(), which allows you to do some initializing the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.

# Example
# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one(return 1,2,3,4,5 etc.):

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# 1
# 2
# 3
# 4
# 5

#
# StopIteration
#
# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration to go forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a spefified number of times:

# Example
# Stop after 20 iterations:

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = MyNumber()
myiter = iter(myclass)
for x in myiter:
    print(x)
# 1
# 2
# 3
# 4
# ...
# 20

