'''
Given a string and a non-negative int n, return a larger string that is n copies of the original string.


stringTimes("Hi", 2) → "HiHi"
stringTimes("Hi", 3) → "HiHiHi"
stringTimes("Hi", 1) → "Hi"

'''


def string_times(str, n):
  
  #Approach 1:
  #Python Short Form:
  #You can multiply a string in python by a constant value.  When you do 
  #this the string is duplicated on itself. 
  #For example:
  #
  #str = "Hello"
  #str = str*3
  #
  #This would result in str becoming "HelloHelloHello"
  #
  #CODE****************
  '''
  return str*n
  #'''
  #END CODE************
  
  #Approach 2: Loop
  #
  #This question highlights two essential ideas.
  # 1. String Construction
  # 2. Loops
  #
  #Tracing the Loop if str = "Hi" and n = 2
  #
  # i = 0, 0 < 2, True, Run Loop
  #   tstr = tstr + str = "" + "Hi" = "Hi"
  # i = 1, 1 < 2, True, Run Loop
  #   tstr = tstr + str = "Hi" + "Hi" = "HiHi"
  # i = 2, 2 < 2, False, Exit Loop
  #
  # It is very important that you can trace basic loops. 
  '''
  tstr = ""
  for i in range(0,n,1):
    tstr = tstr + str
    
  return tstr
  #'''
  
  #Approach 3: While Loop
  #
  # A while loop is a conditional loop.  While loops and for loops 
  # are interchangable.
  #
  #
  '''
  tstr = ""
  i = 0; 
  while (i < n):
    tstr = tstr + str
    i = i + 1
  return tstr
  #'''
  
  
  
