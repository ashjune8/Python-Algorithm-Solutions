# https://www.interviewbit.com/problems/reverse-link-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseBetween(A, B, C):
    lst = []
    newlst = []

    while A != None:
        lst.append(A)
        A = A.next

    templist = lst[B-1:C]
    templist = templist[::-1]

    newlst = lst[0:B-1] + templist + lst[C:]

    for i in range(len(newlst)-1):
        newlst[i].next = newlst[i+1]

    newlst[len(newlst)-1].next = None

    return newlst[0]

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

print reverseBetween(a,2,3).val
    
