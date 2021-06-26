# Global Variables

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# Global variable more example
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)


# The Global keyword

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Pythin is " + x)

# Global keyword more example

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
