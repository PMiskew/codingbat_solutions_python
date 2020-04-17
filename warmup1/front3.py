'''

Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'

'''
def front3(str):
  
  #BIG IDEA:
  #This requires you to first check the length, only then do you pull the values
  #This avoids an index out of bounds error
  '''
  if len(str) <= 3:
    return str + str + str
    
  return str[0:3] + str[0:3] + str[0:3]
  #'''
  
  '''
  if len(str) <= 3:
    return str*3
    
  return str[0:3]*3
  #'''
  
  return str*3 if len(str) <= 3 else str[0:3]*3