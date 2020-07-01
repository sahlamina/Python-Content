# Dictionaries are a bit more dynamic than lists and tuples
# They're very useful with any coding lang
# Simple concept of KEY VALUE PAIRS
# Syntax - {} to create  a dictionary

student_record = {"name": "Agbo",
                  "stream": "DevOps",
                  "completed_lessons": 5,
                  "completed_lesson_names": ["strings", "tuples", "variables"]
                  }

#this is how to select specific items from a dictionary
print(student_record["name"])
print(student_record["completed_lesson_names"][2])


# modifying the dictionary
# student_record["completed_lesson_names"] = 3
# new_list = student_record["completed_lesson_names"]
# print(new_list)

# print(student_record["name"])

# student_record["completed_lesson_names"] = "dictionaries", "lists", "operators"
# mod_list = student_record["completed_lesson_names"]
# print(mod_list)
#
# student_record["completed_lessons_name"].append("Lists")
# student_record["completed_lessons_name"].append("built-in methods")



# print(student_record)
# print(type(student_record))

# this prints the values/ keys
# print(student_record.values())
# print(student_record.keys())