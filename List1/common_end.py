'''
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True

'''

def common_end(a, b):
  
  #Approach 1: Using If
  
  #if a[len(a) - 1] == b[len(b) - 1] or a[0] == b[0]:
  #  return True
  #return False
  
  #Technique:  Since the boolean expression returns True we can simply return
  #the boolean expressions
  
  return a[len(a) - 1] == b[len(b) - 1] or a[0] == b[0]
  