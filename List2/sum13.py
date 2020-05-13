def sum13(nums):
'''

Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6

'''

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
  
  '''
  sum = 0
  i = 0
  
  while (i < len(nums)):
    
    if (nums[i] != 13):
      sum = sum + nums[i]
    else:
      i = i + 1
      
    i = i + 1
      
  return sum
  '''


  #This solution was based on a YouTube comment asking why their code
  #didn't work.  It was using an approximate method to this, but
  #used a for loop and hand some logic issues.   The big idea here is
  #is that you CANNOT change a for loop variable once a loop starts. 
  #The big idea here is that when you remove an element from a list all
  #elements to the right will shift their index. 

  #
  #   0  1  2   3  4  5
  #  [1, 2, 13, 2, 1, 13]
  #  
  #  i = 0  --> 0 < 6 TRUE  --> RUN LOOP
  #    nums[0] == 13 FALSE
  #      SKIP CONDITIONAL CODE BLOCK   
  #    sum = sum + nums[0] = 0 + 1

  #  i = 1 --> 1 < 6 TRUE --> RUN LOOP
  #   nums[0] == 13 FALSE
  #     SKIP CONDITIONAL CODE BLOCK   
  #   sum = sum + nums[1] = 1 + 2 = 3
  
  
  #  i = 2 --> 2 < 6 TRUE --> RUN LOOP
  #   nums[2] == 13 TRUE
  #     ENTER CONDITIONAL CODE BLOCK
  #                                        X  X
  #                               0  1  2  3  4
  #     nums.remove(nums[2]) --> [1, 2, 2, 1, 13] **INDEX SHIFT, LENGTH CHANGE
  #   
  #     2 < 5 TRUE
  #                                       X  X
  #                                 0  1  2  3
  #       nums.remove(nums[2]) --> [1, 2, 1, 13] **INDEX SHIFT, LENGTH CHANGE
  #
  #   2 < 4 and nums[i] != 13 TRUE
  #     sum = sum + nums[i] = 3 + 1 = 4
  
  
  #  i = 3 --> 3 < 4 TRUE --> RUN LOOP
  #   nums[3] == 13 TRUE
  #     ENTER CONDITIONAL CODE BLOCK
  #                       
  #                               0  1  2 
  #     nums.remove(nums[3]) --> [1, 2, 1] **LENGTH CHANGE
  #     
  #      3 < 3 FALSE
  #         SKIP CONDITIONAL CODE BLOCK
  #
  #  3 < 3 and nums[i] != 13 FALSE
  #     SKIP CONDITIONAL CODE BLOCK
  
  #  i = 4 --> 4 < 3 FALSE --> EXIT LOOP
  #     
  # return sum --> 4
  #
  
  if len(nums)== 0:
    return 0
    
  sum=0  
  i = 0
  
  while (i < len(nums)):
    
    if nums[i]==13 :
      
      nums.remove(nums[i])
      
      if i < len(nums): 
        nums.remove(nums[i])
  
    if (i < len(nums) and nums[i] != 13):
      sum = sum+nums[i]
    i = i + 1
  return sum

#THIS IS THE JAVA SOLUTION USED IN MY VIDEO THAT COMPARED PYTHON AND JAVA
'''
public int sum13(int[] nums) {
  
  if (nums.length == 0) {
    return 0;
  }
  
  ArrayList<Integer> list = new ArrayList<Integer>();
  for (int i = 0; i < nums.length; i = i + 1) {
    list.add(nums[i]);
  }
  
  int sum=0; 
  int i = 0; //remove if you use for loop
  
  //for (int i = 0; i < list.size(); i = i + 1) {
  while (i < list.size()) {
    
    if (list.get(i)==13) {
      
      list.remove(i); //remove index i - NOTICE DIFFERENCE FROM PYTHON
      
      if (i < list.size()) { 
        list.remove(i); //remove index i - NOTICE DIFFERENCE FROM PYTHON
      }
    }
    
    if (i < list.size() && list.get(i) != 13) {
      sum = sum+ list.get(i);
    }
    i = i + 1; //remove if you use for loop
  }
  return sum;
}


'''


  
  
      
  
  