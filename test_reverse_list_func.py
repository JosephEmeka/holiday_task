import reverse_list_func

this_List = [22,56,99,101,3,6,7]
this_second_list = [-100, -1, -5, -9, -6, -8, -17]

def test_reverse_list_func():
	assert reverse_list_func.reverse_list_func(this_List) == [7,6,3,101,99,56,22]

def test_reverse_list_func():
	assert reverse_list_func.reverse_list_func(this_second_list) == [-17,-8,-6,-9,-5,-1,-100]	


