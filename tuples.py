# Tuples are like lists but they are immutable
# Tuples are used when you are handling data you would not need to change line DOB/ nhs ID, passport no.

# Syntax of Tuple: we use ()

# Convert the tuple into an string

details = ("name", "dob", "passport number")
details_list = list(details)
print(details_list)

# add your name into the string at 0 index
details_list.insert(0, "Agbo")

# display the list
print(details_list)