'''

Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'


'''

def without_end(str):
  
  '''
        01234
  str = Hello  l = 5  [1:4]
  
        0123
  str = java   l = 4  [1:3]
  
  Generalized: [1: length - 1]
  
  
  '''
  
  
  #Approach 1: 
  slen = len(str)
  return str[1: slen - 1]
  #Approach 2: One Liner
  #return str[1:len(str) - 1]
