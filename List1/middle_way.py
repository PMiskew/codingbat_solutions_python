'''

Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.


middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

'''

def middle_way(a, b):
  
  #Approach 1:
  '''
  c = [a[1],b[1]]
  return c
  '''
  
  #Approach 2;
  
  '''
  c = [] #Create an empty list
  #Caution: You can't access elements that don't exisit so you need to actual
  #         insert them.  So to do this we use the insert function.  
  #         
  c.insert(0,a[1])
  c.insert(1,b[1])
  return c
  '''
  
  #Approach 3:
  #Use append
  '''
  c = []
  c.append(a[1])
  c.append(b[1])
  return c
  '''
  
  #Approach 4: Mod Question - length is odd
  
  #Integer division is the process of dividing two integers and removing 
  #the decimals
  #We know that 3/4 = 0.75, but in programming this can sometimes result in 
  #integer division 3/4 = 0. 
  
  #Python 2: 3/4 = 0 If we divide two integers assume integer result 
  #Python 2: 3.0/4 = 0.75 since 3.0 is a float result is assumed float 
  
  #Python 3: 3/4 = 0.75 In Python 3 it will not do integer division by default
  #Python 3: 3//4 = 0 In Python 3 // means integer division. 
  
  #Codingbat is running Python2 so len(a)/2 is an int divided by an int. 
  #This results in 3/2 = 1, the middle element index. 
  return [a[len(a)/2],b[len(b)/2]]
