'''
QUESTION:

We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False

'''


def monkey_trouble(a_smile, b_smile):
  
  #Theory:  This problem takes two boolens, which means we can map out all 
  #         possibilities and code for them. 
  #
  # a_smile | b_smile | Trouble
  #   F         F         T
  #   F         T         F
  #   T         F         F
  #   T         T`        T
  #
  #Approach 1: Map it all out
  '''
  if a_smile == False and b_smile == False:
    return True
  elif a_smile == False and b_smile == True:
    return False
  elif a_smile == True and b_smile == False:
    return False
  elif a_smile == True and b_smile == True:
    return True
  #'''
  
  #Approach 2: Group True and False situation
  '''
  if a_smile == False and b_smile == False or a_smile == True and b_smile == True:
    return True
  elif a_smile == False and b_smile == True or a_smile == True and b_smile == False:
    return False
  #'''
  
  #Approach 3: Notice that when we look at the truth table there is a relation in 
  #that if the state of the monkeys match we are in trouble.  Therefore we can say
  '''
  if a_smile == b_smile:
    return True
  else:
    return False
  #'''
  
  #Approach 3: Clean up 1
  #Theory: Since a function stops as soon as we reach a return statement we don't 
  #need to include an else statement.  This is the appraoch codes most often use
  '''
  if a_smile == b_smile:
    return True
  return False
  #'''
  
  #Approach 3: Clean up 2:
  #Theory: Since this is evalauating a boolean and returns a boolean we can 
  #simply return the condition we are evaluating
  '''
  return a_smile == b_smile
  #'''
    