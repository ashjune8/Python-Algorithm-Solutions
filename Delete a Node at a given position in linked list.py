def Delete(head, position):
    currentposition = 0
    currentnode = head
    previousnode = head

    if position == 0:

        return head.next

    while currentposition != position:
        currentposition += 1
        previousnode = currentnode
        currentnode = currentnode.next
    previousnode.next = currentnode.next
    return head

