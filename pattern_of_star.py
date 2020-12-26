n = int(input("Enter the number of rows: "))

"""
	Pattern for printing
			*
			**
			* *
			*  *
			*****
"""


for i in range(n):
	for j in range(n):
		if j == 0 or i == (n-1) or i == j:

			print("*", end="")
		else:
			print(end=" ")
	print()

"""
	Pattern for printing
			*****
			 *  *
			  * *
			   **
			    *

"""

for i in range(n):
	for j in range(n):
		if i == 0 or j == (n-1) or i == j:
			print("*", end="")
		else:
			print(end=" ")
	print()

	
"""
	Pattern for printing
			  *
		     * *
		    *   *
		   *     *
		  ********* 


"""

for row in range(1, n+1):
	for col in range(1,2*n):
		if row == n or row+col == n+1 or col-row == n-1:
			print("*", end="")
		else:
			print(end=" ")
	print()

"""
	Pattern for printing
			  *
		     * *
		    *   *
		   *     *
		  * * * * * 

"""

k=2
for row in range(1, n+1):
	for col in range(1,2*n):
		if row+col == n+1 or col-row == n-1:
			print("*", end="")
		elif row == n and col != k:
			print("*", end="")
			k = k + 2
		else:
			print(end=" ")
	print()


"""
	Pattern for printing
			  *
			  **
			  ***
			  ****
"""

row = 0
while(row<n):
	star = row+1
	while star>0:
		print("*", end="")
		star = star - 1

	row += 1
	print()

"""
	Pattern for printing
			    *
			   * *
			  * * *
			 * * * *
"""

row = 0
while row<n:
	space = n-row-1
	while space>0:
		print(end=" ")
		space = space - 1
	star = row + 1
	while star>0:
		print("*", end=" ")
		star = star-1

	row += 1
	print()

"""
	Pattern for printing
			    *
			   * *
			  *   *
			   * *
			    *
"""

for row in range(5):
	for col in range(5):
		if row+col == 2 or col-row == 2 or row-col == 2 or row+col == 6:
			print("*", end="")
		else:
			print(end=" ")
	print()

		

