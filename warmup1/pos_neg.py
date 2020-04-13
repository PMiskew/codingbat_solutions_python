'''
QUESTION:

Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
'''

def pos_neg(a, b, negative):
  
  #Approach 1: 
  #In this approach we first check the negative then make a decision based on 
  #a and b
  '''
  if negative == False:
    if a < 0 and b >=0 or b < 0 and a >= 0:
      return True
    return False
  if negative == True:
    if a < 0 and b < 0:
      return True
    return False
  #'''  
  
  #Approach 2: Optimize Approach 1 - WOULD NOT WORK IN JAVA!
  #In this approach we recognized that the internal conditions return true when 
  #evaluted to true therefore we changed them to a return
  '''
  if negative == False:
    return a < 0 and b >=0 or b < 0 and a >= 0
  if negative == True:
    return a < 0 and b < 0
  #'''
  
  #Approach 3: Optimized Approach 2
  #Though Approach 2 works in python Java would have an issue with it.  Even 
  #though we know negative must be true or false, the compiler doesn't.  This 
  #means one of the if statements might not be executed. Then nothing is 
  #returned which is an issue in many languages, but not python. We simply 
  #remove the second if statement and return the result.  This becuase only if 
  #negative is True will we reach this part of the code. 
  '''
  if negative == False:
    return a < 0 and b >=0 or b < 0 and a >= 0
  return a < 0 and b < 0
  #'''
  
  #Approach 3: Optimization 3
  '''
  if (negative == False): 
    return  (a < 0) ^ (b < 0)
  return a < 0 and b < 0;
  #'''

  
  #Approach 4: One Liner
  #This is really badly designed in that it is hard to read.  It doesn't provide
  #any processing advantage as there are so many steps to do in one line. 
  '''
  return (negative == False and ((a < 0 and b >= 0) or (b < 0 and a >= 0))) or (negative == True and a < 0 and b < 0)
  #'''
  #Approach 4: One Liner using the xor
  '''
  return (not(negative) and ((a < 0) ^ (b < 0))) or (negative and a < 0 and b < 0)
  '''