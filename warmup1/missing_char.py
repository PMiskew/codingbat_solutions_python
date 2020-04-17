
'''


Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'

'''


def missing_char(str, n):
  
  #Approach 1: 
  #This approach highlights your understanding of string construction and 
  #substring
  #newStr = "" #Create an empty strign
  #lstr = len(str)
  #newStr = str[0:n] + str[n+1:lstr]
  #return newStr
  
  #Approach 2: Python Specific Approach 1
  #This approach we have used python specific notiation
  
  #newStr = "" #Create an empty strign
  #newStr = str[0:n] + str[n+1:] #used the [a:] notation to grab from a to end of str
  #return newStr
  
  #Approach 3: One Liner
  return str[0:n] + str[n+1:] 
  

  