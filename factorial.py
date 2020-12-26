import math

n = int(input("Enter the number: "))

"""
	Using inbuilt factorial function in math module.
"""

result = math.factorial(n)
print("The factorial of ",n , "is ", result)


"""
	Using recursion.
"""

def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

result = factorial(n)
print("The factorial of ",n , "is ", result)


"""
	Using only for loops.
"""

result = 1
for i in range(n, 0, -1):
	result = result * i

print("The factorial of ",n , "is ", result)
