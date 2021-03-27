#list

# empty_list = []
#            = list()

courses = ['History', 'Math', 'physics']
print(len(courses))    #op-> 3

# index starts from 0      index-> 0, 1, 2
# we can access last index using -1 courses[-1] inex-> -3 ,-2 ,-1
print(courses[-1])      #op->physics   #if we print a index which is out of scope we will get an error index out of bound

#list.append   it will appedn the item at the end of the list
courses.append('Chemistry')
print(courses)                #op- ['History', 'Math', 'physics', 'Chemistry']

#list.insert(loc, val) if we want to insert an element at specific position
courses.insert(1, 'Test')
print(courses)                #op- ['History', 'Test', 'Math', 'physics', 'Chemistry']

#list1.extend(2ndlist)  merge two lists
list1 = [1, 2, 3]
list2 = [1, 4, 5]
list1.extend(list2)
print(list1)                  #op- [1, 2, 3, 1, 4, 5]

# list.remove(itemValue)     Remove first occurrence of value Raises ValueError if the value is not present
list_1 = [1, 2, 3]
list_1.remove(2)
print(list_1)                 #op- [1, 3]   

# list.pop()       It will remove last element and return it
item = list_1.pop()
print(item)                     # op- 3
print(list_1)                   #op- [1]


num1 = [1, 4, 2, 3, 5, 6]
courses1 = ['math', 'phy', 'chem', 'bio']

# list.reverse()
courses1.reverse()
print(courses1)            #['bio', 'chem', 'phy', 'math']

num1.reverse()
print(num1)                 #[6, 5, 3, 2, 4, 1]

# list.sort()
num1.sort()
print(num1)                 #[1, 2, 3, 4, 5, 6]
courses1.sort()
print(courses1)             #['bio', 'chem', 'math', 'phy']  alphabatically

# list.sort(reverse=True)
num1.sort(reverse=True)
print(num1)                 #[6, 5, 4, 3, 2, 1]
courses1.sort(reverse=True)
print(courses1)             #['phy', 'math', 'chem', 'bio']  alphabatically

# sorted(listName)          #Return a new list containing all items from the iterable in ascending order.
a = sorted(num1)            
print(a)

# list = [1,5,6,7]

# min(list) = 1

# sum(list) = 19

# to find something
#num1 = [6, 5, 4, 3, 2, 1]

# list.index(5) = 1 (returns index otherwise valueError)
print(num1.index(2))                # 4
#print(num1.index(7))                #ValueError: 7 is not in list

# 2 in list   => returns true or False
print(2 in num1)                    #true

# for item in lists:
#     print(item)

for index,item in enumerate(num1):   # use enumerate if we want index also
    print(index, item)
#op-
# 0 6
# 1 5
# 2 4
# 3 3
# 4 2
# 5 1

for index,item in enumerate(num1, start=1):   # use enumerate if we want index also
    print(index, item)         #index will start from 1 now
# op-
# 1 6
# 2 5
# 3 4
# 4 3
# 5 2
# 6 1

#join list as a string
courses = [ 'kp', 'pk', 'lklk']
course_str = ', '.join(courses)     #kp, pk, lklk
print(course_str)

#split string to list
newlist = course_str.split(', ')
print(newlist)                      #['kp', 'pk', 'lklk']
