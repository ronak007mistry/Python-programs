# 1. Using 3rd variable

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

temp = a
a = b 
b = temp

print("After swapping: ")
print("Value of a: ",a)
print("Value of b: ",b)

# 2. Without using 3rd variable

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

a = a+b
b = a-b
a = a-b

print("After swapping: ")
print("Value of a: ",a)
print("Value of b: ",b)