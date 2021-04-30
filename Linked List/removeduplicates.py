# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(A):


    lst = {}
    newlst = []
    

    while A != None:
        if (A.val not in lst.keys()):
            lst[A.val] = 1
            
        else:
            lst[A.val] += 1
        
        A = A.next
            
            
        
    
    for i in lst.keys():
        if(lst[i] == 1):
            newlst.append(ListNode(i))
    
    for i in range(len(newlst)-1):
        newlst[i].next = newlst[i+1]

    if len(newlst) > 0:
        return newlst[0]
    else:
        return None

        
    
    






a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

print (deleteDuplicates(a).val)
