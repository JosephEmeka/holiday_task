import check_duplicates


def test_check_duplicates():

	fruits =['apple', 'orange', 'banana', 'apple', 'apple', 'grape', 'orange']

	assert check_duplicates.check_duplicates(fruits) == ['apple', 'orange']

	names =['John', 'Tolu', 'Ada', 'Ada', 'Dayo', 'Kunle']

	assert check_duplicates.check_duplicates(names) == ['Ada']



	