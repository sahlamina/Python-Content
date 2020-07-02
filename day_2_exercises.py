#write 12a, PG, 18, 15, PG13, U
 # writing a programme to check these conditions by getting user input
 # if age = <= 17 can't watch watch rated 18 movie
 # if age 12 or less can't watch any movies above 12
 # display messages accordingly

age = int(input("How old are you? "))
film_ratings = ["U", "PG", "12a","PG13", "15", "18"]
if age >= 18:
    print("Please join the queue to purchase a ticket")
elif 14 <= age <= 17:
    print("You can watch films in with these ratings ", film_ratings[0:5])
elif 11 < age < 15:
    print("You can watch films in with these ratings ", film_ratings[0:4])
else:
    print("You can watch films in with these ratings ", film_ratings[0:2])


# exercise
# dictionary with employee records 5 key v pairs
# using loop iterate through the dict
# display the values of keys and of the dictionary

employee_record = {"name": "Agbo",
                   "role": "DevOps",
                   "employee_id": 5,
                   "Location": "London",
                   "Age": 24
                  }
for i in employee_record:
    print(i)
print(employee_record.values())
print(employee_record.keys())
