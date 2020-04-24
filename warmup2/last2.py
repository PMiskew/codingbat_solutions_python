'''

Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

#'''

def last2(str):
  
  #Approach 1: 
  #This is an essential concept.  We need to be able to count the number of times
  #a specific instance appears in the string. 
  #
  # 012345
  # hixxhi
  #     hi
  #
  # "hi" == str[0:2] --> True
  # "hi" == str[1:3] --> False
  # "hi" == str[2:4] --> False
  # "hi" == str[3:5] --> False
  #
  
  '''
  ctr = 0
  compStr = str[len(str) - 2: len(str)] #Taking advantage of Python
  
  for i in range(0,len(str) - 2, 1): # i < len(str) - 2, i < 6 - 2 = 4 
    if str[i:i + 2] == compStr:
      ctr = ctr + 1
      
  return ctr
  #'''
  
  #Approach 2: We have modified this slightly to better prepare students to 
  #translate to other languages. 

  #This is necessary if programming in Java, many other languages
  '''
  if (len(str) < 2):
    return 0
    
  ctr = 0
  compStr = str[len(str) - 2: len(str)]
  
  for i in range(0,len(str) - 1, 1):
    if str[i:i + 2] == compStr:
      ctr = ctr + 1
      
  return ctr - 1
  #'''
  
  
  #This approach is wrong in some cases, but a very powerful idea
  

 
  compStr = str[len(str) - 2: len(str)]
  
  newStr = str.replace(compStr,"")
  # 012345
  # hixxhi Lenght = 6
  # 01
  # xx Length = 2
  #
  # 6 - 2 = 4 letters gone
  # 4 / 2 = 2 2 words
  #
  return (len(str) - len(newStr))/2 - 1
  
  
  