# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    visited = []
    startnode = head
    previousnode = head

    currentnode = head

    while currentnode != None:
        if currentnode.val in visited:
            previousnode.next = currentnode.next
            currentnode = currentnode.next



        else:
            visited.append(currentnode.val)
            previousnode = currentnode
            currentnode = currentnode.next



    return startnode


x = ListNode(1)
y = ListNode(1)
x.next = y
print deleteDuplicates(x)

