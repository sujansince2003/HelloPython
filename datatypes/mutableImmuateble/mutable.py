my_list=[1,2,3]
print("Before function:",my_list,"| ID:",id(my_list))
my_list.append(4)
print("After function:",my_list,"| ID:",id(my_list))

# gives same id value as pyhton changed the same object in memory but the address remains same

# list dict are mutable