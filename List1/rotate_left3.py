'''

Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]


'''

def rotate_left3(nums):
  
  #Approach 1: WRONG APPROACH COMMON
  # Often students swap the elements but froget that when you copy an 
  # element into another it over writes it
  #
  # 
  #
  ##Current State nums = [1,2,3] - WE LOSE nums[0]
  #nums[0] = nums[1]
  ##Current State nums = [2,2,3]
  #nums[1] = nums[2]
  ##Current State nums = [2,3,3]
  #nums[2] = nums[0] 
  ##Current State nums = [2,3,2]
  #return nums
  
  #Approach 2: Approach 1 Fixed

  #New line: save nums[0] in a temp variable before we write over it
  temp = nums[0]
  #Current State nums = [1,2,3] - WE LOSE nums[0]
  nums[0] = nums[1]
  #Current State nums = [2,2,3]
  nums[1] = nums[2]
  #Current State nums = [2,3,3]
  nums[2] = temp #change this to copy temp into nums[2] 
  #Current State nums = [2,3,2]
  return nums

   #Approach 3: Thinking about post-conditions.  Big Idea: Lists are reference
  #variables
  new_nums = [nums[1],nums[2],nums[0]]
  return new_nums