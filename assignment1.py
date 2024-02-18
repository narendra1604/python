#Naming conventions

#camel case
myVariableName = "nari"

#pascal case
MyVariableName = "nari"

#Upper case snake
MY_VARIABLE_NAME = "nari"

# Hungarian Notation
strMyString = "nari"
intMyInteger = 123

# ------------------------------------------------------

#Reversing the string using slice method

string = "hello"

reverse_string = string[::-1]

print(reverse_string)


# ---------------------------------------------------------

#  Explore dir() & help()

my_list = [1, 2, 3]
print(dir(my_list))
 
help(list)

# ----------------------------------------------------------------

# List out available attributes for dir()

my_list = [1, 2, 3]
print(dir(my_list))

# ---------------------------------------------------------------
# Experiment those attributes using help()

my_list = [1, 2, 3]

print("Help for '__getitem__':")
help(my_list.__getitem__)

print("\nHelp for '__len__':")
help(my_list.__len__)

