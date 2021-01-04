num = int(input("Enter the number of rows: "))

"""
111
111 222
111 222 333
"""
for i in range(num):
	k = 111
	for j in range(i+1):
		print(format(k, "<5"), end="")
		k += 111
	print()


"""
               111
          111  222
     111  222  333
111  222  333  444
"""

for i in range(num):
	k = 111
	for j in range(num-i-1):
		print(format(" ", "<5"), end="")
	for j in range(i+1):
		print(format(k, "<5"), end="")
		k += 111
	print()



"""
                    111
               222  111
          333  222  111
     444  333  222  111
555  444  333  222  111
"""
for i in range(num):
	k = 111
	for j in range(num-i-1):
		print(format(" ", "<5"), end="")
	k = k*(i+1)
	for j in range(i+1):
		print(format(k, "<5"), end="")
		k -= 111
	print()

