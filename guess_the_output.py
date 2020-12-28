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

# 5. 

list1 = ["These", "are", "a", ["few", "words"], "that", "we", "will", "use"]
print(list1[3:4])
print(list1[3:4][0])
print(list1[3:4][0][1][2])

# 6.

def function(n, list1=[]):
	list1.append(list1.append(n))
	return list1

for i in range(4):
	list2 = function(i)
print(list2)

