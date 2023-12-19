import zeroed_code


def test_zeroed_code_func():

	original_list = [3, 5, 7, 8, 3]
	
	assert zeroed_code.zeroed_code(original_list) == [0, 5, 7, 8, 0]
	