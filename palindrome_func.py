def my_palindrome_func(myString):
  myList = list(myString)
  length = len(myList)
  if myList[length::-1] == myList:
    return True
  else:
    return False



this_string = ("noon")
print(my_palindrome_func(this_string))