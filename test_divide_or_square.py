import divide_or_square


number = 20


def test_divide_or_square_func():
	assert divide_or_square.divide_or_square(number) == 4.47


print(divide_or_square.divide_or_square(number))