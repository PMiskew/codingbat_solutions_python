'''

Given a string, return a string where for every char in the original, there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'

'''

def double_char(str):
  
  output = "" #Step 1: Make an empty string to build
  
  #Step 2:  Look at each letter in teh word and add that letter
  #twince into output
  
  for i in range(len(str)):
    output = output + str[i] + str[i]
  return output
    
  