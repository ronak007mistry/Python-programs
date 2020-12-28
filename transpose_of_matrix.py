p = int(input("Enter the number of rows: "))
q = int(input("Enter the number of columns: "))

matrix1 = [[int(input()) for i in range(q)] for j in range(p)]
print("Matrix 1: ")
for i in range(p):
	for j in range(q):
		print(format(matrix1[i][j], "<4"), end="")
	print()

result = [[0 for i in range(p)] for j in range(q)]
print("Transpose of Matrix 1 is: ")

for i in range(q):
	for j in range(p):
		result[i][j] = matrix1[j][i]

for i in range(q):
	for j in range(p):
		print(format(result[i][j], "<4"), end="")
	print()

