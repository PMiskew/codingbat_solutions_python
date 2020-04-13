'''
Question:

Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True

'''

def makes10(a, b):
  
  #Approach 1:
  # We can check each case and return accordintly.
  
  '''
  if a == 10:
    return True
  elif b == 10:
    return True
  elif a + b == 10:
    return True
  return False
  #'''
  
  #Approach 2: 
  #We can condence the logic using the boolean operator or. 
  '''
  if a == 10 or b == 10 or a + b == 10:
    return True
  else: 
    return False
  #'''
  
  #Approach 3:
  #We can remove the else statement to clean things up a bit
  '''
  if a == 10 or b == 10 or a + b == 10:
    return True
  return False
  #'''
  
  #Approach 2: 
  #Since this function returns a boolean (true or false) and since if the
  #condition evaluates to true we return true.  We can return the boolean expression

  return a == 10 or b == 10 or a + b == 10
  #'''