##
## Python String expandtabs() Method
##

# Example
# Set the tab size to 2 whitespaces:

txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)
# H e l l o

#
# Definition and Usage
#
# The expandtabs() method sets the tab size to the specified number of whitespaces.

#
# Syntax
# >> string.expandtabs(tabsize)

# Parameter Values
# Parameter         Description
# tabsize           Optional. A number specifying the tabsize. Default tabsiize is 8

#
# More Examples
#

# Example
# See the result using different tab sizes:

txt = "H\te\tl\tl\to"
print(txt)
# H       e       l       l       o
print(txt.expandtabs())
# H       e       l       l       o
print(txt.expandtabs(2))
# H e l l o
print(txt.expandtabs(4))
# H   e   l   l   o
print(txt.expandtabs(10))
# H         e         l         l         o