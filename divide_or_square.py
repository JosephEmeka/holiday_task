def divide_or_square(number):

	if number % 5 == 0:
		root = number ** 0.5
		return round(root, 2)
	else:
		remainder = number % 5
		return remainder




myNumber = 22

print(divide_or_square(myNumber))