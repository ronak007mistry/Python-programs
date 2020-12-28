# When gcd of two number is 1, then that two numbers are called Co Prime numbers

from math import gcd

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))


if gcd(num1, num2) == 1:
	print(num1, "and", num2, "are Co prime")
else:
	print(num1, "and", num2, "are not Co prime")

# Co prime of given number in a range


num = int(input("Enter number: "))
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

for i in range(lower, upper+1):
	if gcd(num, i) == 1:
		print(i)

		