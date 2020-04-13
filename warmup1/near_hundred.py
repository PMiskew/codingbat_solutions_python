'''
QUESTION:


Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False


'''
def near_hundred(n):
  
  #Approach 1:
  '''
  if (n < 100):
    if 100 - n <= 10:
      return True
    return False
  elif (n > 100 and n < 190):
    if n - 100 <= 10:
      return True
    return False
  elif (n <= 200 and n > 110):
    if 200 - n <= 10:
      return True
    return False
  elif (n > 200):
    if n - 200 <= 10:
      return True
    return False
  #'''
  
  #Approach 2:
  #Here we use the abs function so we don't have to check the value relative
  #to 100 or 200 to decide if it is 100 - n or n - 100.  
  '''
  if abs(n - 100) <= 10 or abs(n - 200) <= 10:
    return True
  return False
  #'''