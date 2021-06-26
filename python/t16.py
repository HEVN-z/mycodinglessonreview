# Python - String Methods

# String Methods

#
# capitalize()
#
# Python String capitaliize() Methods
# upper case the first letter in this sentence.

from functools import partial
from typing import Text


txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

# Definition and Usage
# Syntax
# string.capitalize()

# More Examples

txt = "36 is my age."
x = txt.capitalize()
print(x)

# ==========================================================

#
# casefold()
#
# Python String casefold() Method
# Make the string lower case:

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# Defination and Usage
# The casefold() method returns a string where all the characters are lower case.
# This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lowercase, and will find more mathces when comparing two strings amd both are converted using the casefold() method.
# Syntax
# string.casefold()

# ==========================================================

#
# casefold()
#
# Python String center() Method
# Print the world "banana", taking up the space of 20 characters, with "banana" in the middle:

txt = "banana"
x = txt.center(20)
print(x)

# Defination and Usage
# The center() method align the string, using a specified character (space is default) as tje fill character.
# Syntax
# string.center(length, character)

# Parameter Values
# Parameter Description
# length    Required. The length of returned string
# character Optional. The character to fill the missing space on the side. Default is " "(space)

# More Example
# Using the letter "O" as the padding character:

txt = "banana"
x = txt.center(20,"O")
print(x)

# ==========================================================

#
# count()
#
# Python String count() Method
# Return the number of time the value "apple" appears in the string:

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# Definition Using
# The count() method returns the number of times a specified value appears in the string.
# Syntax
# string.count(lavue, start, end)

# Parameter Values
# value     Required. A String. The String to value to search for
# start     Optional. An Integer. The position to start the search. Default is 0
# end       Optional. An Integer. The position ti end the search. Default is the end of the string

# More Example
# Search from position 10 to 24:

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

# ==========================================================

#
# encode()
#
# Python String encode() Method
# UTF-8 encode the string:

txt = "My name is Ståle"
x = txt.encode()
print(x)

# Definition and Usage
# The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
# Syntax
# string,encode(encoding=encoding, errors=errors)

# Parameter Values
# encoding  Optional. A String specifying the encoding to use. Default is UTF-8
# errors    Optional. A String specifying the error method. Legal values are:
#           'backslashplace'    - uses a backslah instead of the character that could not be encoded
#           'ignore'            - ignores the characters that cannot be encoded
#           'nameplace'         - replace the character with a text explaining the character
#           'strict'            - Defaukt, raises an error on failure
#           'replace'           - replace the character with a questionmark
#           'xmlcharrefreplace' - replace the character woth an xml character

# More Example\
# These examples uses ascii encoding, and a character that cannot be encodedm showing the result with different errors:

txt = "My name is Ståle"

print(txt)
print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))

# ==========================================================

#
# endwith()
#
# Python String endwith() Method
# Check if the string ends with a punctuation sign(.):

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# Definition and Usage
# The endwith() method returns True if the string ends with the specified value, otherwise False.
# Syntax
# string.expandtabsize(tabsize)

# Parameter Values
# Value     Required. The value to check if the string ends with
# start     Optional. An Integer specifying at which position to start the search
# end       Optional. An Integer specifying at which position ti end the search

# More Examples
# Check if the string ends with ohrase "my world."

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

# Example
# Check if position 5 to 11 ends with the phrase "my world.":

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

# ======================================================================

#
# expandtabs()
#
# Python String expandtabs() Method
# Set the tab size to 2 whitespaces:

txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)

# Definition and Usage
# Parameter Values
# tabsize   Optional. A number specifying the tabsize. Default tabsize is 8

# More Examples
# See the result using different tab size:

txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# ==========================================================================

#
# find()
#
# Python String find() Method
# Where in the text is the word "welcome"?:

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# Definition and Usage
# The find() method finds the first occurrence of the specified value.
# The find() method return -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)
# Syntax
# string.find(value, start, end)

# Parameter Values
# value     Required. The value to search for.
# start     Optional. Where to start the search. Default is 0
# end       Optional. Where to end the search. Default is to the end of the string

# More Examples
# Where in the text is the first occurrence of the letter "e"?:

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

# ============================================================================

#
# format()
#
# Python String format() Method
# Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# Definition and Usage
# Parameter Values
# value1,   Required. One or more valuethat should be formatted and inserted in the string.
# value2..  
#           The values are either a list of values separated by commas, a key=value list, or a comvination of both.
#
#           The values can be of any data type.

# The Placeholders
# The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.

# Example
# Using different placeholder values:

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)

# =====================================================================

#
# format_map()
#
# Formats specified values in a string

# =====================================================================

#
# index()
# 
# Python String index() Method
# Where in the text is word "welcome"?:

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

# Definition and Usage
# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# The index() nethod is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found.(See example below)
# Syntax
# string.index(value, start, end)

# Parameter Values
# value     Required. The value to search for
# start     Optional. Where to start the search. Default is 0
# end       Optional. Where to end the search. Default is to the end of the string

# More Examples
# Where in the text is the first occurrence of the letter "e"?:

txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)

# ======================================================================

#
# isalnum()
#
# Python String isalnum() Method
# Check if all the characters in the text are alphanumeric:

txt = "Company12"
x = txt.isalnum()
print(x)

# Definition and Usage
# The isalnum() method returns True if all the character are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
#
# Example of characters that are not alphanumeric: (soace)!#%&? etc.
# Syntax
# string.isalnum()

# More Examples
# Check if all characters in the text is alphanumeric:

txt = "Company12"
x = txt.isalnum()
print(x)

# ===================================================================

#
# isalpha()
#
# Python String isalpha() Method
# Check if all the characters in the text are letters:

txt = "CompanyX"
x = txt.isalpha()
print(x)

# Definition and Usage
# The isalpha() method returns True if all the characters are alphabet letters (a-z).
# Syntax
# string.isalpha()

# More Examples
# Check if all the characters in the text is alphabetic:

txt = "Company10"
x = txt.isalpha()
print(x)

# ======================================================================

#
# isdecimal()
#
# Python String isdecimal() Method
# Check if all characters in the unicode object are decimals:

txt = "\u0033"
x = txt.isdecimal()
print(x)

# Definition and Usage
# The isdecimal() method returns True if all the characters are decimals (0-9)
# This method is used on unicode objects.
# Syntax
# string,isdecimal()

# More Examples
# Check if all the characters in the unicode are decimals:

a = "\u0030"    # unicode for 0
b = "\u0047"    # unicode for G

print(a.isdecimal())
print(b.isdecimal())

# =======================================================================

#
# isdigit()
#
# Python String isdigit() Method
# Check if all the characters in the text are digits:

txt = "50800"
x = txt.isdigit()
print(x)

# Definition and Usage
# The isdigit() method returnds True if all the characters are digits, otherwise False.
# Exponents, like ², are also considered to be a digit.
# Syntax
# string.isdigit()

# More Examples
# Check if all the characters in the text are digits:

a = "\u0030"    # unicide for 0
b = "\u00B2"    # unicode for ²

print(a)
print(a.isdigit())
print(b)
print(b.isdigit())
print(b.isdecimal())
# =======================================================================

#
# isidentifier()
#
# Python String isidentifier() Method
# Check if the string is a valid identifier:

txt = "Demo"
x = txt.isidentifier()
print(x)

# Definition and Usage
# The isidentifier() method returns True if the string is a valid identifier, otherwise False.
#
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscore (_). A valid identifier cannot start with a number, or contain any spaces.
# Syntax
# string.isidentifier()

# More Examples
# Check if the strings are valid identifiers

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

# ===================================================================

#
# islower()
#
# Python String islower() Method
# Check if all the characters in the text are in lower case:

txt = "hello world!"
x = txt.islower()
print(x)

# Definition and Usage
# The islower() method returns True if all the characters are in lower casem otherwise False.
#
# Numbers, symbols and spaces are not checked, only alphabet characters.
# Syntax
# string,islower()

# More Examples
# Check if all the characters in the texts are in lower case:

a = "Hello world!"
b = "hello 123"
c = "munameisPetter"

print(a)
print(a.islower())
print(b)
print(b.islower())
print(c)
print(c.islower())

# =====================================================================

#
# isnumeric()
#
# Python String isnumeriic() Method
# Check if all characters in the text are numeric:

txt = "565543"
x = txt.isnumeric()
print(txt + " isnumeric()")
print(x)

# Definition and Usage
# The isnumeric() method returns True if all characters are numeric (0-9), otherwise False.
# Exponents, like ² and ¾ are also considered to be numeric values.
# "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and . are not
# Syntax
# string.isnumeric()

# More Examples
# Check if the characters are numeric:

a = "\u0030"    # unicode for 0
b = "\u00B2"    # unicode for ²
c = "10km2"
d = "-1"
e = "1.5"

print(a)
print(a.isnumeric())
print(b)
print(b.isnumeric())
print(c)
print(c.isnumeric())
print(d)
print(d.isnumeric())
print(e)
print(e.isnumeric())

# ============================================================

#
# isprintable()
#
# Python String isprintable() Method
# Check if all the characters in the text are printable:

txt = "Hello! Are you #1?"
x = txt.isprintable()
print(txt + " isprintable()")
print(x)

# Definition and Usage
# The isprintable() method returns True id all the characters are printable, otherwise False.
#
# Example of none printable character can be carriage return and line feed.
# Syntax
# string.isprintable()

# More Examples
# Check if all characters in the text are printable:

txt = "Hello\nAre you #1?"
x = txt.isprintable()
print(txt + " isprintable()")
print(x)

# ===================================================================

#
# isspace()
#
# Python String isspace() Method
# Check if all the characters in the text are whitespace:

txt = "      "
x = txt.isspace()
print(txt + " isspace()")
print(x)

# Definition and Usage
# The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
# Syntax
# string.isspace()

# More Example

txt = "     s     "
x = txt.isspace()
print(txt + " isspace()")
print(x)

# =====================================================================

#
# istitle()
#
# Python String istitle() Method
# Check if each wrd start with an upper case letter:

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(txt + " istitle()")
print(x)

# Definition and Usage
# The istitle() method returns True of all words in a text start with a upper letter, AND the rest of the word are lower case letters, otherwise False.
# Symbols and numbers are ignored.
# Syntax
# string.istitle()

# More Examples
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a + " istitle()")
print(a.istitle())
print(b + " istitle()")
print(b.istitle())
print(c + " istitle()")
print(c.istitle())
print(d + " istitle()")
print(d.istitle())

# =========================================================================

#
# isupper()
#
# Python String isupper() Method
# Check if all the text are in upper case:

txt = "THIS IS NOW!"
x = txt.isupper()
print(txt + " isupper")
print(x)

# Definition and Usage
# The isupper() method returns True if all the characters are in upper case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.
# Syntax
# string.isupper()

# More Examples

a = "Hello World!"
print(a + " isupper()")
print(a.isupper())
b = "hello 123"
print(b + " isupper()")
print(b.isupper())
c = "MY NAME IS PETER"
print(c + " isupper()")
print(c.isupper())

# ===============================================================

#
# join()
#
# Python String join() Method
# Join all items in a tuple into a  string, using a hash character as separator:

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(str(myTuple) + " join()")
print(x)

# Definition and Usage
# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
# Syntax
# string.join(iterable)

# Parameter Values
# iterable  Required. Any iterable object where all the returned values are strings

# More Examples
# Join all item in a dictionary into a string, using a the word "TEST" as separator:

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(str(myDict) + " join()")
print(x)

# =================================================================

#
# ljust()
#
# Python String ljust() Method
# Return a 20 characters long, left justified version of the word "banana":

txt = "banana"
x = txt.ljust(20)
print(txt + " ljust()")
print(x, "is my favorite fruit.")

# Definition and Usage
# The ljust() Method will left align the string, using a specified character (space is default) as the fill character.
# Syntax
# string.ljust(length, character)

# Parameter Values
# length    Required. The length of the returned string
# character Optional. A character to fill the missing space (to the right of the string). Default is " " (space).

# More Examples

txt = "banana"
x = txt.ljust(20, "0")
print(txt + " ljust()")
print(x)

# ===================================================================

#
# lower()
#
# Python String lower() Method
# Lower case the string:

txt = "Hello my FRIENDS"
x = txt.lower()
print(txt + " lower()")
print(x)

# Definition and Usage
# The lower() method returns a string where all characters are lower case.
# Symbols and Numbers are ignored.
# Syntax
# string.lower()

# ===================================================================

#
# lstrip()
#
# Python String lstrip() Method
# Remove spaces to the left of the string:

txt = "           banana           "
print(txt + " lstrip")
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

# Definition and Usage
# The lstrip() method removes any leading characters (space is the default leading character to remove)
# Syntax
# string.lstrip(characters)

# Parameter Values
# characters    Optional. A set of characters to remove as leading characters

# More Examples
# Remove the leading characters:

txt = ",,,,,,ssaaww......banana"
print(txt," lstrip()")
x = txt.lstrip(",.asw")
print(x)

# ===================================================================

#
# maketrans()
#
# Python String maketrans() Method
# Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:

txt = "Hello Sam!"
print(txt, " maketrans(), translate()")
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

# Definition and Usage
# The maketrans() method returns a mapping table that can be use with the translate() method to replace specified characters.
# Syntax
# string.maketrans(x, y, z)

# Parameter Values
# x         Required. If only one parameter is specified, this has to be a dictionary describing how to perform the replace. If two or more parameters are specified, this parameter has to be a string specifying the characters you wnat to replace.
# y         Optional. A string with the same length as parameter x. Each character in the first parameter will replaced with the corresponding character in this string.
# z         Optional. A string describing which characters to remove from the original string.

# More Examples
# Use a mapping table to replace many characters:

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x,y)
print(txt, " maketrans(), translate(), x = mSa, y = eJo")
print(txt.translate(mytable))

# More Example
# The third parameter in the mapping table descripbes characters that you want to remove from the string:

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnight"
print(txt, " maketrans(), translate(), x = mSa, y = eJo, z = odnight")
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))

# More Example
# The maketrans() method itself returns a dictionary describing each replacement, in unicode:

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnight"
zz = "1234567"
print(txt, " maketrans(x ,y ,z)")
print(txt.maketrans(x, y, z))

# ===================================================================

#
# partition()
#
# Python String partition() Method
# Search for the word "banana", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(txt, " partition(\"banana\")")
print(x)

# Definition and Usage
# The partition() method searchs for a specified string, and splits the string into a tuple containing three elements.

# The first element contains the part before the  specified string.

# The second element contains the specified string.

# The third element contains the part after the string.

# Syntax
# string.partition(value)

# Parameter Values
# value     Required. The string to search for

# More Examples
# If the specified value  is not found, the partition() method returns a tuple containing: 1- the whole string, 2- an empty string, 3- an empty string:

txt = "I could eat bananas all day"
print(txt, " partition(\"apples\")")
x = txt.partition("apples")
print(x)

# ===============================================================

#
# replace()
#
# Python String replace() Method
# Replace the word "bananas":

txt = "I like bananas"
x = txt.replace("bananas","apples")
print(txt, " replace(\"bananas\",\"apples\")")
print(x)

# Definition and Usage
# The replace() method replaces a specified phrase with another specified phrase.
# Syntax
# string.replace(oldvalue, newvalue, count)

# Parameter Values
# oldvalue  Required. The string to search for
# newvalue  Required. The string to replace the old value with
# count     Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences.

# More Examoles
# Replace all occurrence of the word "one".

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(txt, "replace(\"one\", \"three\")")
print(x)

# Example
# Replace the two first occurrence of the word "one":

txt = "one one was a race house, two two was one too."
x = txt.replace("one","three",2)
print(txt, "replace(\"one\",\"three\",2)")
print(x)

# ======================================================================

#
# rfind()
#
# Python String rfind() Method
# Where in the text is the last occurrence of the string "casa"M:

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(txt, "rfind(\"casa\")")
print(x)

# Definition and Usage
# The rfind() method finds the last occurrence of the specified value.
# The rfind() method return -1 if the value is not found.
# The rfind() method is almost the same as the rindex() method. See example below.
# Syntax
# string.rfind(value, start, end)

# Parameter Values
# value     Required. The value to search for
# start     Optional. Where to start the search. Default is 0
# end       Optional. Where to end the search. Default is to the end of the string

# More Examples
# Where in the text is the last occurrence of the letter "e"?:

txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(txt,"rfind(\"e\")")
print(x)

# Example
# Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:

txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10)
print(txt,"rfind(\"e\", 5, 10)")
print(x)

# Example
# If the value is not found, the rfind() method return -1, but the rindex() method will raise an exception:

txt = "Hello, welcome to my world."
print(txt, "rfind")
print(txt.rfind("q"))
print(txt, "rindex")
# print(txt.rindex("q"))
# line 925, in <module>
#    print(txt.rindex("q"))
# ValueError: substring not found

# ============================================================================

#
# rindex()
#
# Python String rindex() Method
# Where in the text is the last occurrence of the string "cassa"?:

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(txt, " rindex(\"casa\")")
print(x)

# Definition and Usage
# The rindex() method finds the last occurrence of the specified value
# The rindex() method raises an exception if the value is not found
# The rindex() method is almost the same as the rfind() method. See example below
# Syntax
# string.rindex(value, start, end)

# Parameter Values
# value     Required. The Value to search for
# start     Optional. Where to start the search. Default is 0
# end       Optional. Where to end the search. Default is to the end of the string

# More Examples
# Where in the text is the last occurrence of the letter "e"?:

txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(txt, "rindex(\"e\")")
print(x)

# Example
# Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:

txt = "Hello, welcome to my world."
x = txt.rindex("e",5,10)
print(txt, "rindex(\"e\",5,10)")
print(x)

# Example
# If the value is not found, the rfind() method returns -1 but the rindex() method will raise an exception:

txt + "Hello, welcome to my world."
print(txt, "rfind")
print(txt.rfind("q"))
print(txt, "rindex")
# print(txt.rindex("q"))
#line 978, in <module>
#    print(txt.rindex("q"))
#ValueError: substring not found

# ======================================================================

#
# rjust()
#
# Python String rjust() Method
# Return a 20 characters long, right justified version of the word "banana":

txt = "banana"
x = txt.rjust(20)
print(txt, " rjust(20)")
print(x,"is my favorite fruits.")

# Definition and Usage
# The rjust() method will right align the string, using a specified character (space is default) as the fukk character.)
# Syntax
# string.rjust(length, character)

# Parameter Values
# length    Required. The length of the returned string
# character Optional. A character to fill the mission space (to the left of the string).
#           Default is " "(space)

# More Examples
# Using the letter "O" as the padding character:

txt = "banana"
x = txt.rjust(20,"O")
print(txt," rjust(20,\"O\")")
print(x)

# ========================================================================

#
# rpartition()
#
# Python String rpartition() Method
# Search for the last occurrence of the word "banana", and return a tuple with three elements:
# 1- evething before the "match"
# 2- the "match"
# 3- everything after the "match"

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(txt, " rpartition(\"banana\")")
print(x)

# Definition and Usage
# The rpartition() method searchs for the last occurrencee of a specified string, and splits the string into a tuple contains the part before the specified string.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
# Syntax
# string.rpartition(value)

# Parameter Values
# value     Required. The string to search for

# More Examples
# If the specified value is not found, the rpartition() method returns a tuple containing:
# 1- an empty string.
# 2- an empty string.
# 3- the whole string.

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(txt, " rpartition(\"apples\")")
print(x)

# ========================================================================

#
# rsplit()
#
# Python String rsplit() Method
# Split a string a list, using comma, followed by a space(,) as the separator:

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

# Definition and Usage
# The rsplit() method splits a string into a list, starting from the right.
# If no "max" is specified, this methhod will return the same as the split() method.
# Syntax
# string.rsplit(separator, maxsplit)

# Parameter Values
# separator Optional. Specifies the separator to use when spliting the string. By default any whitespace is a separator.
# maxsplit  Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

# More Examples
# Split the string into a list with maximum 2 items:

txt = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)

# ========================================================================

#
# rstrip()
#
# Python String rstrip() Method
# Remove any whitespace at the end of the string:

txt = "      banana     "
x = txt.rstrip()
print(txt," rstrip()")
print("of all fruits", x, "is my favorite")

# Definition and Usage
# The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
# Syntax
# string.rstrip(characters)

# Parameter Values
# characters    Optional. A set of characters to remove as trailing characters

# More Examples
# Remove the trailing characters if they are commas, s, q, or w:

txt = "banana,,,,,ssqqww....."
x = txt.rstrip(",.qsw")
print(txt, "rstrip(\",.qsw\")")
print(x)

# ==============================================================

#
# split()
#
# Python String split() Method
# Split a string into a list where each word is a list item:

txt = "welcome to the jungle"
x = txt.split()
print(txt, " split()")
print(x)

# Definition and Usage
# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.
# Syntax
# string.split(separator, maxsplit)

# Parameter Values
# separator     Optional. Speficies the separator to use when splitting the string. By default any whitespace is a separator
# maxsplit      Optional. Specifies how many splits to do. Default calue -1, which is "all occurrences"

# More Examples
# Split the string, using comma, followed by a space, as a separator:

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(txt, " split(\", \")")
print(x)

# Example
# Use a hash character as a separator:

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(txt, " split(\"#\")")
print(x)

# Example
# Split the string into a list with max 2 items:

txt = "apple#banana#cherry#orange"
x = txt.split("#",1)
print(txt, " split(\"#\",1)")
print(x)

# =======================================================================

#
# splitlines()
#
# Python String splitlines() Method
# Split a string into a list where each line is a list item:

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(txt, " splitlines()")
print(x)

# Definition and Usage
# The splitlines() method splits a string into a list. The splitting is done at line breaks.
# Syntax
# string.splitlines(keeplinebreaks)

# Parameter Values
# keeplinebreaks    Optional. Specifies if the line breaks should be included (True), or not (False). Default value is False

# More Example
# Split the string, but keep the line breaks:

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True)
print(txt, " splitlines(True)")
print(x)

# =====================================================================

#
# startswith()
#
# Python String startswith() Method
# Check if the string stats with "Hello":

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(txt + " startswith(\"Hello\")")
print(x)

# Definition and Usage
# The startswith() method returns True if the string starts with the specified value, otherwise False.
# Syntax
# string.startswith(value, start, end)

# Parameter Values
# value     Required. The value to check if the string starts with
# start     Optional. An Integer specifying at which position to start the search
# end       Optional. An Integer specifying at which position to end the search

# More Examples
# Check if position 7 to 20 starts with the charcters "wel":

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(txt, " startswith(\"wel\", 7, 20)")
print(x)

# =====================================================================

#
# strip()
#
# Python String strip() Method
# Remove spaces at the beginning and at the end of the string:

txt = "     banana     "
x = txt.strip()
print(txt, " strip()")
print(x)

# Definition and Usage
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
# Syntax
# string.strip(characters)

# Parameter Values
# characters    Optional. A set of characters to remove as leading/trailing characters

# More Examples
# Remove the leading and trailing characters:

txt = ",,,,,rrttgg.....banana.....rrr"
x = txt.strip(",.grt")
print(txt, " strip(\",.grt\")")
print(x)

# ==============================================================

#
# swapcase()
#
# Python String swapcase() Method
# Make the lower case letters upper case and the upper case letters lower case:

txt = "Hello My Name Is PETTER"
x = txt.swapcase()
print(txt, " swapcase()")
print(x)

# Definition and Usage
# The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
# Syntax
# string.swapcase()

# =================================================================

#
# title()
#
# Python String title() Method
# Make the first letter in each word upper case:

txt = "Welcome to my world"
x = txt.title()
print(txt, " title()")
print(x)

# Definition and Usage
# The title() method returns a string where the first character in every word in upper case. Like a header, or a title.
# If the word contains a number or a symbol, the first letter after that will be converted to upper case.
# Syntax
# string.title()

# More Examples
# Make the first letter in each word upper case:

txt = "Welcome to my 2nd world"
x = txt.title()
print(txt, " tilte()")
print(x)

# Example
# Note that the first letter after a non-alphabet letter is converted into a case letter:

txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(txt, " title()")
print(x)

#===================================================================

#
# translate()
#
# Python String translate() Method
# Replace any "S" characters with a "P" character:
# use a dictionary with ascii codes to replace 83 (S) with 80 (P):

mydict = {83:80}
txt = "Hello Sam!"
print(txt, "translate(mydict)")
print(txt.translate(mydict))

# Definition and Usage
# The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
# Use the maketrans() method to create a mapping table.
# If a character is not specified in the dictionart/table, the character will not be replaed.
# If you use a dictionary, you must use ascii codes instead of characters.
# Syntax
# string.translate(table)

# More Examples
# Use a mapping table to repllace "S" with "P":

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt, " translate(mytable)")
print(txt.translate(mytable))

# Example
# The third parameter in the mapping table describes characters that you want to remove from the string:

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt, "maketrans(x, y, z)")
print(x)

# Example
# The same example as above, but using a dictionary instead of a mapping table:

txt = "Good night Sam!"
mydict = {109:101,83:74,97:111,111:None,100:None,110:None,103:None,104:None,116:None}
print(txt, " translate(mydict)")
print(txt.translate(mydict))

# ======================================================================

#
# upper()
#
# Python String upper() Method
# Upper case the string:

txt = "Hello my friends"
x = txt.upper()
print(txt, " upper()")
print(x)

# Definition and Usage
# The upper() returns a string where all characters are in upper case.
# Symbols and Numbers are ignored.
# Syntax
# string,upper()

# =====================================================================

#
# zfill()
#
# Python String zfill() Method
# Fill the string with zeros until it is 10 characters long:

txt = "50"
x = txt.zfill(10)
print(txt, "zfill(10)")
print(x)

# Definition and Usage
# The zfill() method adds zeros(0) at beginning of the string, until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.
# Syntax
# string.zfill(len)

# Parameter Values
# len       Required. A number specifying the desired length of the string

# More Examples
# Fill the strings with zeros until they are 10 characters long:

a = "hello"
b = "welcome to the jungle"
c = "10,000"

print(a, "zfill(10)")
print(a.zfill(10))
print(b, "zfill(10)")
print(b.zfill(10))
print(c, "zfill(10)")
print(c.zfill(10))

