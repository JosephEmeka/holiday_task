def concatenate_func(my_first_list, my_second_list):
	my_first_list = my_first_list + my_second_list
	return my_first_list


this_list = [9,11,5,-5,14,22,7,8]
this_second_list = [10, 3,2,88,9,0]

print(concatenate_func(this_list, this_second_list))