# Definition for singly-linked list.
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

    if l1 == None and l2 ==None:
        return l1
    node1 = l1
    list1 = []
    node2 = l2
    list2 = []
    finallist = []

    while node1 != None:
        list1.append(node1)
        node1 = node1.next
    while node2 != None:
        list2.append(node2)
        node2 = node2.next
    temp = ListNode

    finallist = list1 + list2
    for i in range(len(finallist)-1,0,-1):
        for j in range(i):
            if finallist[j].val > finallist[j+1].val:
                temp = finallist[j+1]
                finallist[j+1] = finallist[j]
                finallist[j] = temp
    i = 0
    while i < len(finallist)-1:
        finallist[i].next = finallist[i+1]
        i += 1

    finallist[len(finallist)-1].next = None

    return finallist[0]
a = ListNode(2)
b = ListNode(1)
print mergeTwoLists(a,b)




