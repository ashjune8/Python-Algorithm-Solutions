# https://www.interviewbit.com/problems/swap-list-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(A):
    
    lst = []
    tempNode = A
    while tempNode != None:
        lst.append(tempNode)
        tempNode = tempNode.next
    i = 0
    while i < len(lst) - 1:
        if(lst[i] != None and lst[i+1] != None):
            temp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp
        i = i + 2

    for i in range(len(lst)-1):
        lst[i].next = lst[i+1]

    return lst[0] 


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

print swapPairs(a).val

