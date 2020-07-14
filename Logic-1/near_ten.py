'''

Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod


near_ten(12) → True
near_ten(17) → False
near_ten(19) → True

'''
def near_ten(num):
  
  
  #Approach 1: Standard if approach
  '''
  if num%10 == 8 or num%10 == 9 or num%10==0 or num%10==1 or num%10 == 2:
    return True
  return False
  '''
  
  #Approach 2: 
  #return num%10 == 8 or num%10 == 9 or num%10==0 or num%10==1 or num%10 == 2
  
  #Approach 2:
  #Since we are looking for 8, 9, 0, 1 ,2 we can't simply set up a range of 
  #values. By adding 2 we are shifting the the values so 
  # 8 --> 10
  # 9 --> 11
  # 0 --> 2
  # 1 --> 3
  # 2 --> 4
  #
  #To account for the 10 and 11 case we mod by 10 again to get the 1's digit. 
  # 8 --> 10 --> 0
  # 9 --> 11 --> 1
  # 0 --> 2
  # 1 --> 3
  # 2 --> 4
  #
  #19 % 10 = 9
  #19 % 10 + 2 = 11
  #(19 % 10 + 2) % 10 = 1
  
  return 0 <= (num%10 + 2) % 10 <= 4
  
  
  
  
  
  