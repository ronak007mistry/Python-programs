def BinarySearch(list1, key):
	low = 0
	high = len(list1)-1
	Found = False

	while low<=high and not Found:
		mid = (low + high) // 2
		if key == list1[mid]:
			Found = True
		elif key > list1[mid]:
			low = mid + 1
		else:
			high = mid - 1

	if Found:
		print("Key is found ")
	else:
		print("Key is not found")




num = int(input("Enter the list length: "))
list1 = [int(input()) for i in range(num)]

list1.sort()
print(list1)
key = int(input("Enter the Key: "))

BinarySearch(list1, key)
