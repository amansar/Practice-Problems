function solves reverse linked list problem
def reverseLLS(head):
  if(head == none):
    print("LLS IS EMPTY")
  elif( head.next == none):
    return head
  else:
    preve = head
    temp = head.next
    head.next = none
    while(temp != none):
      preve = temp
      temp = temp.next
      prev.next = head
      head = prev
    return head
