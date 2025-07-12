x=4
print(f"before:x={x}")
print(f"{id(x)}")
x=x+1
print(f"before:x={x}")
print(f"{id(x)}")

# immutable
# when the value changed then it will create a new object and new address is shown for id(object) because the as value changed variable is pointing to new object address in memory. 
# int str tuple are immutable