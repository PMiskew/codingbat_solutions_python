'''
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;


front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'

'''


def front_times(str, n):
  
  #Approach 1: Using Python Short hand
  
  #return str[0:3] * n
  
  #Approach 2: Using String Construction and Loop
  
  tstr = ""
  
  for i in range(0,n,1):
    tstr = tstr + str[0:3]
    
  return tstr