"""
perfect number is a positive integer that is equal to the sum of its positive divisors 
excluding the number itself.
"""
# number entered by the user

num = int(input("Enter the number: "))
result = 0

for i in range(1, num):
	if (num % i) == 0:
		result = result + i

if result == num:
	print(num, "is the perfect number")
else:
	print(num, "is not the perfect number")


# number in a range

lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

for num in range(lower, upper+1):
	result = 0
	for i in range(1, num):
		if (num % i) == 0:
			result = result + i

	if result == num:
		print(num, "is the perfect number")
	else:
		print(num, "is not the perfect number")