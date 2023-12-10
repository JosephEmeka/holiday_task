import largest_func

this_List = [22,56,99,101,3,6,7]

this_second_list = [-100, -1, -5, -9, -6, -8, -17]

def test_largest_func():
	assert largest_func.largestFunc(this_List) == 101

def test_largest_func():
	assert largest_func.largestFunc(this_second_list) == -1	

print(largest_func.largestFunc(this_List))

print(largest_func.largestFunc(this_second_list))