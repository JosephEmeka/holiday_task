import my_discount

price = 250000

discount = 45

def test_my_discount_func():
	assert my_discount.my_discount(price, discount) == 137500

