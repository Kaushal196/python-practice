#tuples

# we can not modify tuples  immutable 
# list are mutable

# empty_tuple = ()
#             = tuple()

tuple_1 = ('History', 'Math')
tuple_2 = tuple_1

# print both
print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'   #error tuple does not support item assignment

# we can apply/use only those operations of list which will not modify the tuple
