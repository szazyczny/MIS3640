# #Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

# # diff21(19) → 2
# # diff21(10) → 11
# # diff21(21) → 0

def diff21(n):
    '''
    Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
    '''
  dif = abs(n - 21)
  if n <= 21:
    return dif
  else:
    return dif * 2

print(diff21(19)) 
print(diff21(10)) 
print(diff21(21))



#Cigar Party
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return True
  else:
    if 40 <= cigars <= 60:
      return True
    else:
      return False

print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))