import concatenate_func
 
list_one = [1, 3, 9]
list_two = ["big","small"]

def test_concatenate_func ():
	assert concatenate_func.concatenate_func(list_one, list_two) == [1, 3, 9, "big", "small"]