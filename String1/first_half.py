

def first_half(str):
  
  #Approach 1:
  #This approach we will break up the solutoin to a couple lines
  #Note, the key piece here is that the string is of even lenght so it divides
  #in half easily
  #The fact that the problem is telling you this means it is a PRE-CONDITION
  
  #lstr = len(str)
  
  #result = str[0:lstr/2]
  #return result
  

  #Approach 2: One Line
  return str[0:len(str)/2]