'''

Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0

'''

def count_evens(nums):
  
  '''
  FOCUS - LIST AND LOOPS
  
  Question - Do I have to look at every element?  If the answer is yes then
  a loop is your solution. 
  
  for i in range(0, len(nums), 1): 
    <LOOP CODE>
  
          0  1  2  3  4
  nums = [2, 1, 2, 3, 4]    len = 5
  
  i = 0 
    0 < 5 TRUE - RUN LOOP
      is 2 even 
        TRUE - COUNT = COUNT + 1
  i = 1
    1 < 5 TRUE - RUN LOOP
      is 1 even 
        FALSE
  i = 2
    2 < 5 TRUE - RUN LOOP
      is 2 even 
         TRUE - COUNT = COUNT + 2
  i = 3
    3 < 5 TRUE - RUN LOOP
      is 3 even 
         FALSE
  i = 4 
    4 < 5 TRUE - RUN LOOP
      is 4 even 
         TRUE - COUNT = COUNT + 1
  i = 5
    5 < 5 FALSE - EXIT LOOP
    
  '''
  
  count = 0
  
  for i in range(0, len(nums), 1):
    if (nums[i] % 2 == 0):
      count = count + 1
  
  return count
      
  
  
  
  