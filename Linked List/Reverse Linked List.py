# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    temp = []
    if head == None:
        return head

    while(head != None):
        temp.insert(0,head)
        head = head.next

    i = 0
    while(i<len(temp) - 1):
        temp[i].next = temp[i+1]
        i += 1

    temp[len(temp)-1].next = None

    return temp[0].val

x = ListNode([])



print reverseList(x)



