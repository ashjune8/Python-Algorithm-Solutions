# https://www.interviewbit.com/problems/reorder-list/

import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reorderList(A):

    if A == None or A.next == None:
        return A

    lst = []
    while A != None:
        lst.append(A)
        A = A.next
    
    reverlst = lst[::-1]

    i = 0
    cycle = math.floor((len(lst)-1)/2)
    
    while i < cycle:
        lst[i].next = reverlst[i]
        reverlst[i].next = lst[i+1]
        reverlst[i+1].next = None
        i += 1

    return lst[0]

    
    