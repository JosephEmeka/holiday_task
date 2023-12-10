import even_positions_func

my_new_list = [9,11,5,-5,14,22,7,8]
this_second_list = [-100, -1, -5, -9, -6, -8, -17]

def test_even_positions_func():
	assert even_positions_func.even_positions_func(my_new_list) == [9, 5, 14, 7]