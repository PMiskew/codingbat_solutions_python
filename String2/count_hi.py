'''

Return the number of times that the string "hi" appears anywhere in the given string.


count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2

'''
def count_hi(str):

  #Approach 1: Use the count function
  '''
  return str.count("hi")
  '''
  
  #Approach 2: Learn Reading Frames
  #Reading Frames
  #
  # Looking for the word "hi" that means I need to look at two letters at 
  # a time
  #
  # 012345678
  # abc hi ho
  # XX     XX
  #
  # str[0:2] substring is inclusive:exclusive
  # str[7:9]
  #
  #
  #
  '''
  ctr = 0
  
  for i in range(0, len(str) - 1, 1):
    #i = 0 str[0:2]
    #i = 1 str[1:3]
      temp = str[i: i + 2]
      if temp == "hi":
        ctr = ctr + 1
      

  return ctr
  '''
  
  #Approach 3: Collapsing a String
  
  # 012345678 l = 9
  # abc hi ho
  
  # 0123456 l = 7
  # abc  ho
 
  str1 = str.replace("hi","") 
  return (len(str) - len(str1))/2
  
    

    
    
    