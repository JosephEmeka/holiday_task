import check_element_func

this_list = [9,11,5,-5,14,22,7,8]


def test_check_element_func():
	assert check_element_func.check_element_func(this_list, 5) == True	
	assert check_element_func.check_element_func(this_list, -9) == False
	assert check_element_func.check_element_func(this_list, "NO") == False

 

 

