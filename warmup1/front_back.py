'''

Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

'''


def front_back(str):
  
  #Genearl Comment:  This question is tricky so make sure you understand
  #what is happening. I STRONGlY suggest you map out a few to understand the 
  #indexing
  # 0123     3120  
  # code --> eodc
  #
  # We are swapping the first and last characeter. 
  #
  # STRING CONSTURCTION:  THIS IS A VERY IMPORTANT CONCEPT.  IT IS WHEN YOU
  #                       BUILD A NEW STRING BY TAKING PARTS OF EXISISTING ONES
  
  #Approach 1: 
  #
  lstr = len(str)
  if lstr < 2:
    return str
    
  newStr = str[lstr - 1] + str[1:lstr - 1] + str[0]
  return newStr
