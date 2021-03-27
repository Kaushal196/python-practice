#key valye pairs
students = {'name': 'Kaushal', 'age': 25, 'courses': ['Math', 'CSE']}
print(students)
print(students['name'])
#students['ddd']  #key error if not found

print(students.get('name'))
print(students.get('ddd'))   # return none 
print(students.get('ddd', 'Not found'))  #if key not found return Not found

#update a new key
students['phone'] = '2222'

#update existing key
students['name'] = 'sanu'
print(students)

#update dic
students.update({'name': 'Kaushal123', 'age': 30, 'courses': ['Math', 'CSE', 'Eng'], 'phn': '22222'})
print(students)

#delete a key
del students['age']
#age = students['age']

#len(students) no of keys
#students.keys() => returns all the keys
#students.values() => returns values
#students.items() => return both
print(students.items())
#op dict_items([('name', 'Kaushal123'), ('courses', ['Math', 'CSE', 'Eng']), ('phone', '2222'), ('phn', '22222')])

for key in students:
    print(key)          #prints only key

for key, value in students.items():
    print(key, value)       # prints key and value