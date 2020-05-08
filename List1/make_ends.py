'''
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.


make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]

'''
def make_ends(nums):
  
  #Approach 1:
  lennums = len(nums)
  nums1 = [nums[0], nums[lennums - 1]]
  return nums1
  #Approach 2: One Liner
  #return [nums[0], nums[len(nums) - 1]]
