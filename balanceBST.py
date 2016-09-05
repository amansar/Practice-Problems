Program takes array as input and inserts elements in to a BST in a way that the tree is balaned and height is minimal

def balance(arr, middle, left, right):
  if(len(arr) == 1):
    toReturnNode = BSTNode(arr[0])
    return toReturnNode
  else:
    middle = len(arr)/2
    left = middle - 1
    right = middle + 1
    realRoot = arr[middle]
    leftN = balance(arr[0:left], middle, left, right)
    newRoot = BSTNode(realRoot)
    newRoot.left = leftN
    rightN = balance(arr[right:len(arr)], middle, left, right)
    newRoot = BSTNode(realRoot)
    newRoot.right = rightN
    
def main():
  arr = input.split(' ')
  middle = len(arr)/2
  left = middle - 1
  right = middle + 1
  balance(arr, middle, left, right)
  
  main()
