def largestFunc(anyList):
	largest = float('-inf')
	for items in anyList:
		if items > largest:
			largest = items
	return largest


myList =[1,300,41,2,8,9,5]

this_second_list = [-100, -1, -5, -9, -6, -8, -17]

print(largestFunc(myList))
	

print(largestFunc(this_second_list))
		