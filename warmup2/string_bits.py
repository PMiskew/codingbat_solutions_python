'''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

#'''

def string_bits(str):
  
  #Approach 1: Better and more efficent
  #Concept: 
  # When do I need a loop?
  # You need a loop if you have to point at each letter when you try to find 
  # the solution
  #
  # In this case I want to take each second letter starting at index 0. We
  # can write a loop that increments by 2 each time
  '''
  tstr = ""
  for i in range(0, len(str), 2):
    tstr = tstr + str[i]
    
  return tstr
  #'''
  
  #Approach 2: Good concept, but poorly designed code.
  #
  # Every second letter is in an even index.  We can check if the index is even
  # and then add it to the new string.  This is less efficient because now the 
  # loop has to go through every element
  '''
  tstr = ""
  
  for i in range(0,len(str),1):
    if i % 2 == 0:
      tstr = tstr + str[i]
      
  return tstr
  #'''
  
  