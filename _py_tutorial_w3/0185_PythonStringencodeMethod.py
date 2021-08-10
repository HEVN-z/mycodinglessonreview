##
## Python String encode() Method
##

# Example
# UTF-8 encode the string:

txt = "My name is Stăle"
x = txt.encode()
print(x)
# b'My name is st\xc4\x83le'

#
# Definition and Usage
#
# The encode() method encodes the string, using the specified encoding. If no encoding is specidied, UTF-8 will be used.

#
# Syntax
# >> string.encode(encoding=encoding, errors=errors)

#
# Parameter Values

# Parameter                 Description
# encoding                  Optional. A string specifying the encoding to use. Default is UTF-8
# errors                    Optional. A string specifying the error method. Legal values are:
#                   'backslashreplace'  - uses a backslash instead of the character that could not be encoded
#                   'ignore'            - ignores the characters that cannot be encoded
#                   'namereplace'       - replaces the character with a text explaining the character
#                   'strict'            - Default, raises an error on failure
#                   'replace'           - replaces the character with a questionmark
#                   'xmlcharrefreplace' - replaces the character with an xml character

#
# More Examples
#

# Examplle
# These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:

txt = "My name is Stăle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
# b'My name is St\\u0103le'
print(txt.encode(encoding="ascii",errors="ignore"))
# b'My name is Stle'
print(txt.encode(encoding="ascii",errors="namereplace"))
# b'My name is St\\N{LATIN SMALL LETTER A WITH BREVE}le'
print(txt.encode(encoding="ascii",errors="replace"))
# b'My name is St?le'
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
# b'My name is St&#259;le'
