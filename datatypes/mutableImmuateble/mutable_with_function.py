def modify_list(lst):
    print("Inside before:", lst, "| ID:", id(lst))
    lst.append(4)
    print("Inside after:", lst, "| ID:", id(lst))

my_list = [1, 2, 3]
print("Before function:", my_list, "| ID:", id(my_list))
modify_list(my_list)
print("After function:", my_list, "| ID:", id(my_list))
