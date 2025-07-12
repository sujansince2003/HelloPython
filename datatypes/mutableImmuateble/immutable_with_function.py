def modify_number(n):
    print("Inside before:", n, "| ID:", id(n))
    n = n + 10
    print("Inside after:", n, "| ID:", id(n))

x = 5
print("Before function:", x, "| ID:", id(x))
modify_number(x)
print("After function:", x, "| ID:", id(x))

