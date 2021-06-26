# Python - Format - Strings

# String Format

# age = 36
# txt = "My name is John, I am " + age
# print(txt)
## TypeError: can only concatenate str (not "int") to str ##

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} of item {} for {} dollar."
print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))