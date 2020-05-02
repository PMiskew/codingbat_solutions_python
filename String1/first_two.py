'''

Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".


first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'
'''
def first_two(str):
  
  #Big Idea: Length check
  #You need to check the lenght before you access the first two characters.  
  #If you do you will get an index out of bounds error
  
  if len(str) > 1: 
    return str[0:2]
    
  return str
  
  #Python Thing: WORKS BECAUSE DIFFENT
  #Python is very forgiving in that if you access a substring and it goes beyond
  #the index values it just gives you what is there.  ALL OTHER LANGUAGES CRASH.
  #so the below line works, but only because it is python.  If str = "x" it would
  #crash in Java or C
  #Approach 2:
  #return str[0:2]
  
  #Python Thing: CRASHES LIKE ALL OTHERS
  #Python does crash if you try to access an index which is out of bounds. This
  #is much like other languages.  These means the below approach won't work
  #Approach 3: Won't work!
  #return str[0] + str[1]
  
  