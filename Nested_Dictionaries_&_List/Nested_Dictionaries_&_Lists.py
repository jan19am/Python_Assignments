# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# First Task
x[1][0] = 15
print(x)


# Second Task
students[0]['last_name'] = 'Bryant'
print(students)


#Third Task
sports_directory['soccer'] [0] = 'Andres'
print(sports_directory)


# Fourth Task
z[0]['y']= 30
print(z)


# 2. Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for student in students:
    # print(student)
        for key, val in student.items():
            print(key, "-", val)

iterateDictionary(students)


# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for student in students:
        for key, val in student.items():
            if key == key_name:
                print(val)

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


# 4. Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, values in dojo.items():
        print(len(values), key + '\n')
        for value in values:
            print(value + '\n')

printInfo(dojo)

