'''
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.


extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'

'''


def extra_end(str):
  
  #Best Practice: Always pull the lenght of the string and 
  #store it in a variable. 
  l = len(str)
  
  #       01234
  #str = "Hello" to get the last two letters str [3:5]
  #str = "ab" to get the last two letters str[0:2]
  #
  #Question: What is the common pattern happening here?
  #         The second value is always the length of the word
  #         The first value is the lenght - 2
  #
  # Generalize: We can generalize this to [lenght - 2: length]
  #             We know the result will always be two letters because
  #             lenght - (length - 2) = length - length + 2 = 2
  #
  
  return str[l-2:l] +str[l-2:l] +str[l-2:l]

  #Python Short Cut: In python there is a shortcut in that we can multiply strings
  #                  by a constant to duplicate it.  So we can shorten the above  
  #                  line to 
  
  #return str[l-2:l] * 3