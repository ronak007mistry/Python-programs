p = int(input("Enter the row number for matrix 1: "))
q = int(input("Enter the column number for matrix 2: "))
n = int(input("Enter the column number for matrix 1/ row number of matrix 2: "))

print("Enter the elements for matrix 1: ")
matrix1 = [[int(input()) for i in range(n)] for j in range(p)]
print("Matrix 1: ")
for i in range(p):
	for j in range(n):
		print(format(matrix1[i][j], "<5"), end="")
	print()

print("Enter the elements for matrix 2: ")
matrix2= [[int(input()) for i in range(q)] for j in range(n)]
print("Matrix 2: ")
for i in range(n):
	for j in range(q):
		print(format(matrix2[i][j], "<5"), end="")
	print()


result = [[0 for i in range(q)] for j in range(p)]
for i in range(p):
	for j in range(q):
		for k in range(n):
			result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]

print()
print("Result of matrix 1 and matrix2 is ")
for i in range(p):
	for j in range(q):
		print(format(result[i][j], "<5"), end="")
	print()

