list1 = []
num = int(input("How many numbers you want to enter: "))
for k in range(num):
	list1.append(float(input("Enter values ")))

print("Unsorted list ", list1)

for j in range(len(list1)-1):
	for i in range(len(list1)-1-j):
		if list1[i] > list1[i+1]: # For descending order use list1[i] < list1[i+1]
			list1[i], list1[i+1] = list1[i+1], list1[i]
print("Sorted list ", list1)
