'''
*********
PROGRAM 3
*********
Define a function second_smallest that takes a list of integers or floats as an argument. The function returns the 2nd smallest number in the list.
'''
def second_smallest(nums):
  list.sort(nums, reverse=True)
  print (list[-2])
