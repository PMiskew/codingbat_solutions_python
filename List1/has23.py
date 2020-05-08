'''
Given an int array length 2, return True if it contains a 2 or a 3.


has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False

'''
def has23(nums):
  
  #Approach 1
  '''
  if (nums[0] == 2 or nums[1] == 2):
    return True
  elif (nums[0] == 3 or nums[1] ==3):
    return True
    
  return False
  '''
  
  #Approach 2
  '''
  if (nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] ==3):
    return True
    
  return False
  '''
  
  return nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] ==3