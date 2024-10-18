'''Python - Convert a list of Tuples into Dictionary'''

# The List of Tuples for convart Dictionary 
list_of_tuples = [("N","Name"), ("R","Roll"), ("C","Class")]

# Creating a Empty Dictonary 
dictionary = {}     

# Using loop convert List of tuples to Dictonary
for key, value in list_of_tuples:
    dictionary[key] = value

print("The convarted dictonary is :",dictionary)