# DAta collection

# java uses array, in python lists are the same as Arrays
# both serve the same of storing data
#why lists? they help manage data, access data in order, and they give us option to add, remove data

#syntax of lists: [list] hard brackets, (tuple), {dictionary - key:value} pairs
#Tuples are immutable - can't be changed

# List of cities

# cities = ["Tokyo", "Paris", "Prague", "Luxembourg"]
# #whenever you see the word display in exam, it means they want you to print
#
# # print(cities)
# # print(type(cities))
# # print(cities[3]) # this is how you print an index from a list
# cities[3] = "Amsterdam" # this will replace index 3 with dam
# print(cities)
#
# cities.append("Vilnius")
# print(cities)
#
# cities.remove("Paris")
# print(cities)

# Removes last entry in the list
cities = ["Tokyo", "Paris", "Prague", "Luxembourg"]
cities.pop()
print(cities)

# Inserts entry at a specified index
cities.insert(0, "London")
print(cities)

# Lists can hold multiple data types
# mix_type_string = [1, 2, 3], ["one", "two", "three"]
# print(mix_type_string)

# Here is an example of concatenating two lists of different data types
mix_type_string = [1, 2, 3]
string_list = ["one", "two", "three"]
print(string_list + mix_type_string)