'''
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → Falses
'''
def has22(nums):
  
  #We can exit as soon as we find a 2, 2 situation. 
  #There will be a return statement inside the loop
  
  #         0  1  2  3
  # nums = [1, 2, 1, 2])  lenght = 4
  #         I  X
  #               I  X
  #
  '''
  for i in range(0, len(nums) - 1, 1):
    
    if (nums[i] == 2 and nums[i + 1] == 2):
      return True
  
  
  
  return False
  '''
    
  #         0  1  2  3
  # nums = [1, 2, 1, 2])  lenght = 4
  #         X  I
  #               X  I  
  #
  
  for i in range(1, len(nums), 1):
    
    if (nums[i - 1] == 2 and nums[i] == 2):
      return True
  
  
  
  return False
