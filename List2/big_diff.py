'''

Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8

'''
def big_diff(nums):

  #Approach 1: Learning and Understanding
  #Loop through and find largest and smallest element and then subtract
  #them once loop is done
  
  #When finding the largest/smallest value always initalize the 
  #largest/smallest to an element in the list.  This means you don't need
  #to know anything about the list values
  #
  #Example 
  #   nums = [-1,-4,-3]
  #   If I set largest = 0 we will end up with largest since all values are 
  #   less than 0.  0 IS NOT IN THE LIST!! 
  '''
  largest = nums[0]
  smallest = nums[0]
  
  for i in range(0, len(nums), 1):
    largest = max(largest,nums[i])
    smallest = min(smallest,nums[i])
    
  return largest - smallest
  '''
  
  #Approach 2: Quick CAUTION! DOES NOT RESPECT REFERNCE TYPES
  '''
  nums.sort()
  return nums[len(nums) - 1] - nums[0]
  '''
  
  #Approch 3: Short and Respects Reference Types
  return max(nums) - min(nums)
  
  
  