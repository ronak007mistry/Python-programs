row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

print("Enter the elements for matrix 1: ")
matrix1 = [[int(input()) for i in range(col)] for j in range(row)]
print("Matrix 1: ")
for i in range(row):
	for j in range(col):
		print(format(matrix1[i][j], "<3"), end="")
	print()

print("Enter the elements for matrix 2: ")
matrix2= [[int(input()) for i in range(col)] for j in range(row)]
print("Matrix 2: ")
for i in range(row):
	for j in range(col):
		print(format(matrix2[i][j], "<3"), end="")
	print()


result = [[0 for i in range(col)] for j in range(row)]
for i in range(row):
	for j in range(col):
		result[i][j] = matrix1[i][j] + matrix2[i][j]

print()
print("Result of matrix 1 and matrix2 is ")
for i in range(row):
	for j in range(col):
		print(format(result[i][j], "<3"), end="")
	print()

