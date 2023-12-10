def reverse_list_func(myList):
    length = len(myList)
    for items in myList:
      myNewList = myList[length::-1]
    return myNewList


this_list = [9,11,5,-5,14,22,7,8]

print(reverse_list_func(this_list))




