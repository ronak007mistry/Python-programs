num = (input("Enter the odd length number: "))
length = len(num)
print()
for i in range(length):
	for j in range(length):
		if i==j or i+j==length-1:
			print(num[i], end=" ")
		else:
			print(" ",end=" ")
	print()

print()
print()

for i in range(length):
	for j in range(length):
		if i==j or i+j==length-1:
			print(num[j], end=" ")
		else:
			print(" ",end=" ")
	print()