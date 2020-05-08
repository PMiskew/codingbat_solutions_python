'''

Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.


non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'

'''

def non_start(a, b):
  
  #Approach 1: Broken up
  #lena = len(a)
  #lenb = len(b)
  
  #newStr = a[1:lena] + b[1:lenb]
  #return newStr
  
  #Approach 2: One Liner
  return a[1:len(a)] + b[1:len(b)]
  
  