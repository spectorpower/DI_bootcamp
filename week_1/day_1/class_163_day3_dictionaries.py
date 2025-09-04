# DICTIONARIES: COMPLEX DATA STRUCTURE.
# it allows us to "label" the data insied the structure
# use {'key', 'value'}
# user_info = ['Nikita', 'email', 'phone', ('city', 'city2')] #not useful much 
# now we can write down in dictionaries in a usefull way
#user_info = {'full name': 'Nikita',
#             'email': 'bb@gmail.com',
#             'city': ('tlv', 'rishon'),
#            'phone': '875875875',
#             }
# SYNTAX: {key:value,
#          key:value,
#          }
# ACCESSING DATA INSIDE DICTIONARIES
#print(user_info['email'])
#print(user_info['city'][1]) #only second city
# ADD KEY:VALUE

#user_info['family'] = ['Bob', 'Sam', 'Pete']
# user_info.update({'hobbies':{'yoga', 'gaming', 'sleeping'}})

# print(user_info)

# CHANGING DATA INSIDE DICTIONARIES
# user_info['family'].append('John')
# user_info['family'][1] = 'Slartibartfast'

# METHODS
#print.(user_info['email'].upper()) # prints in upper case 
#user_info['balance'] += 10000 #adds numbers

# LOOPS IN DICTIONARIES
# Keys ()

student_info = { 'first_name': 'Harry',
                 'last_name': 'Potter', 
                 'age': 14, 
                 'address' : 'Privet Drive, 4',
                 'pets': ['Hedwig', 'Buckbeak'],
                 'houses': {'main': 'Griffyndor', 'second': 'Slytherin'},
                   'best_friends': ('Ron Weasley', 'Hermione Granger') 
                   }

for key, value in student_info.items():
    print(key, value)


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
        del sample_dict[key]
print(sample_dict)

# ADVANCED
# other very usefull build-in methods
# ENUMERATE() - allows access to the index and the element of  sequence

students = ['Harry', 'Ron', 'Hermione', 'Draco', 'Luna']
for i, name in enumerate(students):
      students[i] = f'Welcome {name}'
print(students)

# ZIP
grades = [100,85,90,60,75]
students_new = ['Harry', 'Ron', 'Hermione', 'Draco', 'Luna']
students_new_grades = dict(zip (students_new, grades))
print(students_new_grades)

# LIST COMPREHENSION

# LONG
numbers = list(range(1,10))
squared_numbes = []
for num in numbers:
      squared = num ** 2
      squared_numbes.append(squared)
print(squared_numbes) 

# SHORT
squared_numbes = [num ** 2 for num in numbers]
print(squared_numbes)
