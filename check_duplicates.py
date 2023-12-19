def check_duplicates(my_list):

	duplicates = [] 

	for item in my_list: 

		if my_list.count(item) > 1 and item not in duplicates:
		
		 duplicates.append(item) 


		if len(duplicates) > 0: 

			return duplicates 

		else: 

			return "No duplicates"
	



fruits =['apple', 'orange', 'banana', 'apple']

names = ['Yoda', 'Moses', 'Joshua', 'Mark']


print(check_duplicates(fruits))


print(check_duplicates(names))

