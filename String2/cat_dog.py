

'''

Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

'''

def cat_dog(str):
  
  #Approach 1: Built in string methods
  '''
  return str.count("cat") == str.count("dog")
  '''
  
  #Approach 2: This is a standard count instance and compare results technique
  #
  # 012345678 
  # cataaadog length = 9
  # XXX   XXX
  #
  # [0:3] [6:9]
  # Length of reading frame? The reading frame is three.
  #
  '''
  dog_count = 0
  cat_count = 0
  #Trick: len(str) - ((reading frame length) - 1)
  for i in range(0, len(str) - 2, 1):
    if str[i: i + 3] == "cat":
      cat_count = cat_count + 1
    if str[i: i + 3] == "dog":
      dog_count = dog_count + 1
  
  return dog_count == cat_count
  '''

  #Approach 3: replace trick
  #If we replace cat with an empty string and then separatly replace dog
  #with an empty string we can compare their lenght.  If it is the same 
  #you removed the same number of cats and dogs. 
  #Example:
  # str = "catdogcat"
  # strNoCat will become "dog"
  # strNoDog will become "catcat"
  # since the length isn't same same we didn't remove the same amount of cat as dog
  
  no_cat = str.replace("cat","")
  no_dog = str.replace("dog","")
  
  return len(no_cat) == len(no_dog)
  
  
  
