# GCD = Greatest Common Divisor or HCF = Higest Common Factor
# 1. Method

import math
print(math.gcd(4, 18))
print(math.gcd(64, 48))

# 2. Method

def ComputeGCD(a, b):
	if b == 0:
		return a
	else:
		return ComputeGCD(b, a%b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(ComputeGCD(num1, num2))