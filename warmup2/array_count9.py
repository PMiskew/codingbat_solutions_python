'''

Given an array of ints, return the number of 9's in the array.


array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3


'''

def array_count9(nums):
  
  '''
  Big Idea: Looping through an array and inspecting every elements
    
    FOR LOOP
      IF
    
  nums = [1, 2, 9]
  
  nums[0] == 9 --> 1 == 9 --> FALSE 
  nums[1] == 9 --> 2 == 9 --> FALSE 
  nums[2] == 9 --> 9 == 9 --> TRUE --> CTR = CTR + 1 
  
  '''
  
  ctr = 0
  for i in range(0, len(nums), 1):
  
    if nums[i] == 9:
      ctr = ctr + 1
    
  return ctr;
