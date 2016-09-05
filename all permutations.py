Recursive function for generating all permutations of an input string. 
def allPermutations(word):
if(len(word) <= 1):
  return word
else:
  perms = allPermutations(word[1:])
  char = word[0]
  result = []
  for perm in perms:
    for i in range(len(perm)+1):
      result.append(perm[:i] + chr + perm[i:]
return result
