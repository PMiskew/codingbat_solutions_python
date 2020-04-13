'''
QUESTON:

The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''

def sleep_in(weekday, vacation):
  
  #Long Approach:
  #We can do this by testing every single case.  This will work for small 
  #siutaitons like this, but is not always practical.  Does anyone see a 
  #pattern in the output here?
  #
  # weekday | vacation | result
  #   F           F       T
  #   F           T       T
  #   T           F       F
  #   T           T       T
  #
  '''
  if weekday == False and vacation == False:
   return True
  if weekday == False and vacation == True:
    return True
  if weekday == True and vacation == False:
    return False
  if weekday == True and vacation == True:
    return True
  #'''
  
  #Shorter Approach:
  #We notice that only one case returns false
    #if weekday == True and vacation == False:
    #  return False
    #else:   
    #  return True
    
    
  #Optimization 1:
  #Theory: As soon as we hit a return statement were done. 
  '''
  if weekday == True and vacation == False:
    return False
  
  return True #Catch all return 
  #'''
  
  #Optimization 2:
  #Trick:  If we are returning a boolean we can return the boolen expression 
  #        with the if statement. 
  '''
  return not(weekday == True and vacation == False)
  #'''
    