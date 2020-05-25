'''
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.


cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True

'''
def cigar_party(cigars, is_weekend):
  
  if is_weekend == False:
    #return cigars >= 40 and cigars <= 60 # 40 <= cigars <= 60
    return 40 <= cigars <= 60
  
  #What about the weekend?
  return cigars >= 40
 