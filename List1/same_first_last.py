
'''

Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True

'''

def same_first_last(nums):
  
  #Step 1: 
  x = len(nums)
  
  #Step 2: Conditional Check
  #Best Practice: ALWAYS CHECK LENGHT FIRST!!!
  if (len(nums) >= 1 and nums[0] == nums[x - 1]):
    return True
  
  return False
    
  
  #One Liner: This works because when we see a return statement the program
  #           always evaluates the return statement then returns it.  Since
  #           this function returns True or False we can return the boolean 
  #           statement with the if. 
  #return len(nums) >= 1 and nums[0] == nums[len(nums) - 1]