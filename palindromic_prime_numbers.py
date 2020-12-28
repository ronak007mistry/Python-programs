lower = int(input("Enter the lower range: "))
upper = int(input("Enter the uppee range: "))

for num in range(lower, upper+1):
	reverse = int(str(num)[::-1])

	if num == reverse:
		if num>1:
			for i in range(2, num):
				if (num%i) == 0:
					print(num, "is not a prime number! but is a palindrome number")
					break
			else:
				print(num, "is palindromic prime number")

else:
	if num>1:
			for i in range(2, num):
				if (num%i) == 0:
					print(num, "is not a prime number! and also is not a palindrome number")
					break
			else:
				print(num, "is prime number and not a palindrome.")

