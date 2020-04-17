'''
QUESTION:

Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'

'''

def not_string(str):
  
  #String Theory:
  # Remember when we think of strings in any language we think of length and 
  # index.  For example
  #
  #        01234
  # str = "HELLO"
  #
  # HELLO has a length of 5 and index 0 to 4
  
  #Approach 1: 
  #check if the string starts with not.  If the does then return the string
  #otherwise concatinate not on the front. 
  '''
  if str[0:3] == "not":
    return str
  return "not " + str
  #'''
  
  #Approach 2: Modification to Approach 1(BEST PRACTICE)
  #Caution, when using python you can access a substring outside the index
  #and it is forgiving.  JAVA IS NOT.  Also, with Python if you access an index
  #outside the bounds individiually it will crash.  Always length check before
  #accessing values or ensure the pre-considition clearly states the length 
  #requirements. 
  
  '''
  if len(str) >= 3 and str[0:3] == "not":
    return str
  return "not " + str
  #'''
  
