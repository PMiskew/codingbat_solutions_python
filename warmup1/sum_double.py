
'''
QUESTION:

Given two int values, return their sum. Unless the two values are the same, then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''

def sum_double(a, b):
  
  sum = a + b
  
  if a == b:
    return 2 * (sum) #As soon as a return statement is reached the method stops!

  return sum

  