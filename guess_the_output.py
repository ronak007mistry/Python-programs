# 1.

x = []
if x:
	print(x, "True")
else:
	print(x, "False")


# 2.

p = (1, 10)
q = 0
r = []
if p or q or r:
	print("True")
else:
	print("False")

# 3. Infinite program

# list1 = ["abc", "123"]
# for i in list1:
# 	list1.append(i)
# print(list1)

# 4. 

for i in range(1, 20):
	if i == 5:
		break
	else:
		print(i)

else:
	print("Hello")

