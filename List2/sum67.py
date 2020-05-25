'''

Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4

'''
def sum67(nums):
  
  #Approach 0: Using a while loop
  #See video in comment Codingbat Compare. In this video we go through
  #a more complex approach, and use it to discuss the difference between
  #java and python. 
  #shttps://www.youtube.com/watch?v=6cZJ9FmvXX8&t=2s
  
  #Approach 1:
  '''
  count = True
  sum = 0
  
  for i in range(0, len(nums), 1):
    
    if nums[i] == 6:
      count = False
    elif count == False and nums[i] == 7:
      count = True
    elif count == True:
      sum = sum + nums[i]

  
  return sum
  '''
