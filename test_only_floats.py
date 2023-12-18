import only_floats


def test_only_floats_func ():

	a = 2.3

	b = 10

	assert only_floats.only_floats(a, b) == 1