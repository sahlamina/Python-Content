# # Sets are very similar to lists
# # What's the difference - sets are unordered
# # syntax: we use {}
#
# car_part = {"wheels", "windows", "doors"}
# print(car_part)
#
# # with sets, we can add items with sets
# car_part.add("seats")
# print(car_part)
# car_part.discard("windows")
# print(car_part)

#Frozen set

# counting = frozenset([1, 2, 3, 4, 5])
# print(counting)

# what are loops
# for loops are used to iterate through lists, strings, dictionaries and tuples
#syntax: for variable in name of the data_collection (list, string, dictionary or tuple)
#
# list_data = [1, 2, 3, 4, 5]
# for data in list_data:
#     if data > 4:
#         break
#     elif data < 0:
#         print( "Please enter value above 0")
#
#     print(data)

# print data block should be within if block

# create a string and loop through the string
# print the string in one line
city = "london"
# for element in city:
#     print(element)

# for index in city:
#     in_one_line += " " + index
#     if city[-1] == index:
#         print(in_one_line)

student_record = {"name": "Agbo",
                  "stream": "DevOps",
                  "completed_lessons": 5,
                  "completed_lesson_names": ["strings", "tuples", "variables"]
                  }
# this give the first letter of every key
for record in student_record:
    print(record[0])

# exercise
# dictionary with employee records 5 key v pairs
# using loop iterate through the dict
# display the values of keys and of the dictionary

student_record = {"name": "Agbo",
                  "role": "DevOps",
                  "employee_id": 5,
                  "": ["strings", "tuples", "variables"]
                  }

While



#syntax - () store them in a variable