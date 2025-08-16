# Variables - are containers for storing data values
# Python has no command for declaring a variable, unlike some programming languages like Java, C++
#Variables do not need to be declared with any particular type,
# and can even change type after they have been set.
x = 5  # x is integer / int
x = 'Mark'  # x is string / str
123
#Casting
#If we want to specify the data type of a variable, this can be done with casting:
x = str(3)  # x will be '3' str
y = int(3)  # y will be 3 int
z = float(3)    # z will be 3.0 float

# Get the Type
# You can get the data type of a variable with the type() function.

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Case-Sensitive / Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a

# Variables in Python are dynamic
x = 5   #can be set as int
x = 'Bob'     #then as str

# Variable names
# 1. Must start with a letter or underscore:
name = 'John'
_names = ['John', 'Bob']

# 2. Cannot start with a number
2_names = ['John', 'Bob']   #

# 3. Can only contains alphanumerical characters and underscore
'''
- a-Z
- 0-9
- _
'''
# my_var    # ok
# my var or my-var  # not ok


# Multiword variable names
# camelCaseFont
# PascalCase
# snake_case


# Many Values to Multiple Variables
# Python allows us to assign values to multiple variables in one line:
x, y, z = 'Banana', 'Apple', 'Ananas'
print(x, y, z)

# And you can assign the same value to multiple variables in one line:
x = y = z = 'Banana'

































