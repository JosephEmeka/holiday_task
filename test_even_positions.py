import even_positions_func

my_new_list = [9,11,5,-5,14,22,7,8]

def test_even_positions():
	assert even_positions_func.even_positions_func(my_new_list) == [9, 5, 14, 7]