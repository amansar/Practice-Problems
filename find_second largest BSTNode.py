#input is the root node of the binary search tree and the assumption is I have a binary search tree node that has a value, left, and right.
#Class BSTNode:
  #def __init__(self, val):
    #self.value = val
    #self.left = none
    #self.right = none

def find_largest(root_node):
  current = root_node
  while (current != none):
    if(current.right == none):
      return current.value
    current = current.right
def find_second_largest(root_node):
  #checks that there're at least two nodes in tree
  if(root_node.left == none or root_node.right == none):
    raise Exception("Must have at least two nodes")
  current = root_node
  #traverses through tree until second largest is found
  while (current != none):
  `#checks if current node in tree has only a left tree and no right tree
   #if so, it'll find the largest node in the left tree since at this point the largest node is current
    if(current.left != none and current.right == none):
      return find_largest(current.left)
    #checks if upcoming node is largest by making sure the upcoming node has no children
    #if this is the case, then the current node is the second larggest and it'll be returned
    elif(current.right != none and current.right.left == none and current.right.right == none):
      return current.value
    current = current. right
