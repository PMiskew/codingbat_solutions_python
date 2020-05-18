def has22(nums):
  
  #         0  1  2  3
  # nums = [1, 2, 1, 2]
  #         X  X
  #
  
  
  for i in range(0, len(nums) - 1, 1):
    if nums[i] == 2 and nums[i + 1] == 2:
      return True
      
  return False
