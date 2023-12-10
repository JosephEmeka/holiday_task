import running_total_func

this_List = [22,56,99,101,3,6,7]

def test_running_total_func():
	assert running_total_func.running_total_function(this_List) == [22, 78, 177, 278, 281, 287, 294]