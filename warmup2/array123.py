'''


Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True

'''

def array123(nums):
  
  #Big Idea:  Placing the return statement.  When deciding where to place the
  #return statement ask youself if you can stop looking as soon as you find
  #what you are looking for.  If that is the case, you can return right away
  
  #Big Idea: A Reading Frame is what I refer to as how many elements are 
  #inspected at a time. In this case we are looking for the sequence 1, 2, 3
  #which means we have a reading frame of three. 
  #
  #   index = 0  1  2  3  4 
  #    nums = 1, 1, 2, 4, 1
  #           X  X  X
  #
  #
  
  #Quick rule: len(nums) - (reading frame length - 1)
  for i in range (0, len(nums) - 2, 1):
    if (nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3):
      return True
      
  return False