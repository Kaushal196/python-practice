# sets
# empty_set = {}   // not correct it will create empty dict
#           = set()
# unordered, no duplicate

set_1 = {'History', 'Math'}

# sets are best optimized to check an element is present or not
print('Math' in set_1)              #True

s1 = {1, 2, 3}
s2 = {2, 4}
print(s1.intersection(s2))          #{2}
print(s1.difference(s2))            #{1, 3}
print(s1.union(s2))                 #{1, 2, 3, 4}