string = input("Enter the string: ")
result = dict()
count = 0

vovels = "a", "e", "i", "o", "u"
for i in range(len(string)):
	
	if string[i] in vovels:
		count = count + 1

print("total vovels", count)

