def count_code(str):
  
  count = 0
  
  for i in range(0, len(str) - 3, 1):
    
    if str[i: i + 2] == "co" and str[i + 3] == "e":
      count = count + 1
      
      
  return count
