#  Modules - .py file is module 
# Package - collection of .py files or modules + __init__.py files



import myModules
myModules.say_Hello("Samiksha")
myModules.say_Bye("Ray")

from myModules import person1
print(person1["DOB"])






# Library - collection of modules + packages that provide pre written functionality 
# of your program . Libraries are typical larger and more feature- rich than 
# package or modules 

# Why Library - 
# to avoid writing common functionalities from stratch 
# to leverage powerfull tools developed by community 

# Example of popular libraries are - 
# Pandas - For data menipulation 
# Matplotlib - For plotting and visualization 

# using a library 

# import pandas as pd


import math

a = 36 
print(math.sqrt(a))

from math import factorial
b = 5
print(factorial(b))


import seaborn as sb