lower = int(input("Enter the lower interval: "))
upper = int(input("Enter the upper interval: "))

for num in range(lower, upper+1):
	if num > 1:
		for i in range(2, num):
			if(num%i) == 0:
				print(num, "is not a prime number")
				break

		else:
			print(num, "is a prime number")