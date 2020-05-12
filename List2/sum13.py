def sum13(nums):
  
  
  #
  #         0  1   2  3  4  5
  # nums = [1, 13, 2, 2, 1, 13]  --> 1 + 2 + 1 = 4
  #                                    
  # i = 0    0 < 6 TRUE - RUN LOOP
  #     nums[0] != 13 TRUE
  #         sum = 1
  #
  # i = 1    1 < 6 TRUE - RUN LOOP
  #     nums[0] != 13 FALSE
  #         i = i + 1 = 2
  #
  # i = 3    3 < 6 TRUE - RUN LOOP
  #     nums[3] != 13 TRUE
  #       sum = 1 + 2 = 3
  #
  # i = 4    4 < 6 TRUE - RUN LOOP
  #     nums[4] != 13 TRUE
  #       sum = 3 + 1 = 4
  #
  # i = 5    5 < 6 TRUE - RUN LOOP
  #
  #     nums[5] != 13 FALSE
  #       i = i + 1 = 5 + 1 = 6
  #
  # i = 7    7 < 6 FALSE EXIT LOOP
  #  
  # I am first going to write this using a for loop.  In Java this would
  # work perfectly.  In Python it does not! This is an important idea.
  '''
  sum = 0
  
  for i in range(0, len(nums), 1):
    
    if (nums[i] != 13):
      sum = sum + nums[i]
    else:
      i = i + 1
      
    #Loop applies change at the end of the loop block
  
  return sum
  '''
  # YOU CANNOT MANIPULATE THE COUNTING VARIABLE IN A FOR LOOP IN PYTHON
  #
  #
  
  
  sum = 0
  i = 0
  
  while (i < len(nums)):
    
    if (nums[i] != 13):
      sum = sum + nums[i]
    else:
      i = i + 1
      
    i = i + 1
      
  return sum
  
  
      
  
  