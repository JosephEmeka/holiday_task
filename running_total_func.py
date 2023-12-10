def running_total_function(my_list):
    running_total = 0
    total_list = []
    for items in my_list:
        running_total += items
        total_list.append(running_total)
    return total_list

my_list = [1, 2, 3, 4, 5]
result = running_total_function(my_list)
print(result) 

this_list = [22,56,99,101,3,6,7]
result = running_total_function(this_list)
print(result)  