class ListNode(object):
 def __init__(self, x):
     self.val = x
     self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    finalresult = []

    if l1 == None and l2 == None:
        return l1
    if l1 == None:
        finalresult.append(l2)
        l2 = l2.next

    elif l2 == None:
        finalresult.append(l1)
        l1 = l1.next
    elif l1.val > l2.val:
        finalresult.append(l2)
        l2 = l2.next
    else:
        finalresult.append(l1)
        l1 = l1.next
    while l1 or l2:
        if l1 == None:
            finalresult.append(l2)
            l2 = l2.next

        elif l2 == None:
            finalresult.append(l1)
            l1 = l1.next
        elif l1.val > l2.val:
            finalresult.append(l2)
            l2 = l2.next
        else:
            finalresult.append(l1)
            l1 = l1.next
        finalresult[len(finalresult) - 2].next = finalresult[len(finalresult) - 1]
    finalresult[len(finalresult)-1].next = None

    return finalresult[0]

a = ListNode(None)
b = ListNode(1)
print mergeTwoLists(a,b)

