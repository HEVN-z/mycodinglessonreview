# Python Strings
# Strings

print("Hello")
print('Hello')

# Assign String to a Variable

a = "Hello"
print(a)

# Multiline Strings

a = """Lorem ipsum dolar sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolar sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# String are Arrays

a = "Hello, World!"
print(a[1])

# Looping Through a String

for x in "banana":
    print(x)

# String Length

a = "Hello, World!"
print(len(a))

# Check String

txt = "The best things in life are free!"
print("free" in txt)

print("\n")
print("\n")
print("\n")
print("\n")

print(4j+1j)
print(4+1j)
print(4j+1)

print("\n")
print("\n")
print("\n")
print("\n")

print(1e0)
print(1e1)
print(1e2)
print(1e3)
print(1e4)

print("\n")
print("\n")
print("\n")
print("\n")

print(1+4j == 1j+4)

print(1j+4j == 4j+1j)

print(True | False)

print("\n")
print("\n")
print("\n")
print("\n")

a = 'b'
if a is not 'a':
    print('a is not a, a = ' + a)
if a != 'a':
    print('a is not a, a = ' + a)

a = 'a'
if a is 'a':
    print('a is a, a = ' + a)
if a == 'a':
    print('a is a, a = ' + a)

# Check String

txt = "The best things in life are free!"
print("free" in txt)

# Looping Through a String

for x in "banana":
    print(x)

# String Length

a = "Hello, World!"
print(len(a))

#Check String

txt = "the best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if NOT

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, \"expensive\" is NOT present.")
