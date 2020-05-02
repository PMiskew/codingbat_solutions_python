'''

Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]


'''
def reverse3(nums):
  
  #Approach 1: Using temp variable
  #Technical Issue: This will work on coding bat, hwoever, typically we have to
  #be very careful changing a list (or any reference type) that is passed into 
  #a function
  
  #temp = nums[0]
  #nums[0] = nums[2]
  #nums[2] = temp
  #return nums

  #Approach 2: Make new list
  #nums1 = [nums[2],nums[1],nums[0]]
  #return nums1
  
  #Approach 3: OneLiner
  return [nums[2], nums[1], nums[0]]