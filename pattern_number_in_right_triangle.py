n = int(input("Enter the number of rows: "))
"""Pattern for printing
	1
	12
	123
	1234
	12345
"""
for i in range(1, n+1):
	for j in range(1, i+1):
		print(j, end="")
	print()



"""Pattern for printing
	1
	22
	333
	4444
	55555
"""

for i in range(1, n+1):
	for j in range(1, i+1):
		print(i, end="")
	print()


"""Pattern for printing in Floyd's triangle
	1
	23
	456
	78910
	1112131415
"""

num = 1
for i in range(1, n+1):
	for j in range(1, i+1):
		print(num, end=" ")
		num = num+1
	print()


"""Pattern for printing 
	12345
	1234
	123
	12
	1
"""

for row in range(n, 0, -1):
	for col in range(1, row+1):
		print(col, end="")
	print()


"""Pattern for printing 
	55555
	4444
	333
	22
	1
"""

for row in range(n, 0, -1):
	for col in range(1, row+1):
		print(row, end="")
	print()


"""Pattern for printing 
	Python

	P
	Py
	Pyt
	Pyth
	Pytho
	Python
"""
string = input("Enter the string: ")
length = len(string)
for row in range(length):
	for col in range(row+1):
		print(string[col], end="")
	print()



"""Pattern for printing in Floyd's triangle in nice shape
	1
	23
	456
	78910
	1112131415
"""


num = 1
for i in range(n):
	for j in range(i+1):
		print(format(num, "<4"), end="")
		num = num+1
	print()




"""Pattern for printing
	1
	2 6
	3 7 10
	4 8 11 13
	5 9 12 14 15
"""

for row in range(n):
	val = row+1
	dec = n-1
	for col in range(row+1):
		print(val, end=" ")
		val = val+dec
		dec = dec-1
	print()


"""Pattern for printing
	1
	2 9
	3 8 10
	4 7 11 14
	5 6 12 13 15
"""


for i in range(n):
	for j in range(i+1):
		x=0
		for k in range(j):
			x = x+n-k
		if j%2 == 0:
			print(x+i-j+1, end=" ")
		else:
			print(x+n-i, end=" ")
	print()


"""Pattern for printing
	15
	14 10 
	13 9 6
	12 8 5 3
	11 7 4 2 1
"""

def num(n1):
	if n1 == 1:
		return 1
	return n1 + num(n1-1)

k = num(n)	
for row in range(n):
	val = k-row
	dec = n-1
	for col in range(row+1):
		print(format(val, "<3"), end="")
		val = val-dec
		dec = dec-1
	print()

