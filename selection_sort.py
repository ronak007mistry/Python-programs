# 1. Using min() function (It will not work on repetitive elements)

list1 = [56,3,2,45,78,0,33,56.96]
print(list1)

for i in range(len(list1)-1):
	min_val = min(list1[i:]) # for max use max(list1[i:])
	min_ind = list1.index(min_val)
	if list1[i] != list1[min_ind]:
		list1[i], list1[min_ind] = list1[min_ind], list1[i]

print(list1)


# 2. For duplicate values

list1 = [56,3,2,45,3,45,78,78,0,33,56.96]
print(list1)

for i in range(len(list1)-1):
	min_val = min(list1[i:]) # for maximum value use max(list1[i:])
	min_ind = list1.index(min_val, i)
	if list1[i] != list1[min_ind]:
		list1[i], list1[min_ind] = list1[min_ind], list1[i]

print(list1)


# 3. Without using built-in methods


num = int(input("How many numbers you want to enter? "))
list1 = [float(input("Enter number ")) for x in range(num)]
print(list1)

for i in range(len(list1)-1):
	m_val = list1[i]
	for j in range(i+1, len(list1)):
		if list1[j] < m_val:  # for maximum value use list1[j] > m_val
			m_val = list1[j]

	m_ind = list1.index(m_val, i)
	if list1[i] != list1[m_ind]:
		list1[i], list1[m_ind] = list1[m_ind], list1[i]

print(list1)