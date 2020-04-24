'''
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

'''


def string_splosion(str):
  
  #Approach 1: We will write a loop to move through each index and take the 
  #substring from 0 to the loop counter.  Watch we need to increase the loop 
  #counter by 1 to get the whole string added. 
  
  tstr = ""
  
  for i in range(0,len(str)+1,1):
    tstr = tstr + str[0:i]
    
  return tstr
