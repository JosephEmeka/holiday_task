def even_positions_func(myList):
  for items in myList:
    my_items = myList[0::2] 
  return my_items


my_new_list = [9,11,5,-5,14,22,7,8]

print(even_positions_func(my_new_list))