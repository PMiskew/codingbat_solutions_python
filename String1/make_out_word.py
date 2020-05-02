'''

Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".


make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'

'''
def make_out_word(out, word):
  
  #Some students
  #This is beautiful and simple.  However, this is python centric meaning 
  #there are things there that don't translate well.  Caution, use python
  #stuff, but don't get too comfortable.  
  #return out[0:2] + word + out[-2:]
  
  #More Common
  #Problem: The precondition for out is it is always four characters. 
  #         0123
  #         <<>>
  #         This means [2:4] gets the last two characters. 
  #         From a design perspective this is great!
  return out[0:2] + word + out[2:4]
  
  
  #Best for understanding
  #                               4 - 2 = 2:4
  return out[0:2] + word + out[len(out) - 2: len(out)]
  
