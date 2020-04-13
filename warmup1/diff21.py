'''
Question

Given two int values, return their sum. Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8

'''

def diff21(n):
  
  #Note:  All the other exampels returned booleans so far.  This example
  #       returns an intger.  Always pay attention to the return type. 
  
  #Approach 1:This is a case where we need to first check the value of n
  #once we know that we can decide if we send the absolute difference or
  #the absolute different*2
  
  '''
  if n > 21:
    return (n - 21)* 2
  return 21 - n
  #'''
  
  #Approach 2:  Modification of approach 1.
  #Notice that in both cases we calculate the different and the order matters
  #based on the size of n. We can use the absolute function, a build in function
  #in the standard library. We can store the absolute different in a variable and
  #use that. 
  
  '''
  diff = abs(n - 21)
  if n > 21:
    return diff*2
  return diff
  #'''
  
  #Approch 1: Python supports a single line conditional statement that we can
  #use in this case.
  '''
  return abs(n-21)*2 if n > 21 else abs(n-21)
  #'''
  
  #Approach 2: I am proud of this one, but it is horribly designed in terms
  #of readability.
  '''
  return int(abs((n)-21)*round(min(abs(n)/21+0.5,2)))
  #'''
  
  #LONGER EXPLAINATION
  
  #return abs((n)-21)
  #return round(min(abs(n)/21+0.5,2))
  
  '''
  Powerful idea, have seen it on the AP exam

  x = round(n + 0.5) 
  n = 1.1    round(1.1 + 0.5) = round(1.6) = 2.0
  n = 1.51   round(1.51 + 0.5) = round(2.01) = 2.0
  n = 0.95   round(0.95 + 0.5) = round(1.45) = 1.0
  
  n = 22
    
    round(min(abs(22)/21+0.5,2)))
    round(min(22/21 + 0.5, 2)))
    round(min(1.0476 + 0.5, 2)))
    round(min(1.5476,2))
    round(1.547)
    2.0
    
  n = 2
  
    round(min(abs(2)/21+0.5,2)))
    round(min(2/21+0.5,2)))
    round(min(0.0952+0.5,2)))
    round(min(0.5952,2))
    round(0.5952)
    1.0
  
  n = -2
  
    round(min(abs(-2)/21+0.5,2)))
    round(min(2/21+0.5,2)))
    round(min(0.0952+0.5,2)))
    round(min(0.5952,2))
    round(0.5952)
    1.0
  
  '''

