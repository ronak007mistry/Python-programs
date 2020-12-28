list2 = []

def get_max(list1):
	for i in list1:
		if type(i) == list:
			get_max(i)
		else:
			list2.append(i)

	return max(list2)


list1 = [1,2,[34,5],545,[34,46,[777,9,56],43],67,67,3,2,6,67]
print(get_max(list1))


