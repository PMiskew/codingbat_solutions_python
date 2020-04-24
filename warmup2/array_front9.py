'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False

'''

def array_front9(nums):
  '''
  Two Big Things
  1.  The function can exit as soon as a 9 is found!
  2.  We only want to loop through the first four elements, or if the list 
      is smaller just the length
  '''
  '''
  l = 4
  
  if len(nums) < 4:
    l = len(nums)
  

  #l = min(4,len(nums))

  for i in range(0,l,1):
    if nums[i] == 9:
      return True
      
  return False
  '''
  
  return 9 in nums[0:4]
  
  
  
  
  
  
  

