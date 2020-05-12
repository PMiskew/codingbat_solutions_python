'''

Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2


'''

def count_code(str):
  
  
  # co?e
  # 
  # Modification: Counting the number of times a specific substring appears in 
  #               a larger string
  #
  

  # 0123456789
  # aaacodebbb  length = 10
  # XX?X  XX?X
  #
  # [0:4] [6:10]
  
  count = 0
  
  for i in range(0, len(str) - 3, 1):
    
    if (str[i] == 'c' and str[i + 1] == 'o' and str[i + 3] == 'e'):
      count = count + 1
      
  return count
    