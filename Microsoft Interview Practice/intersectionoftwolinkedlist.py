# https://leetcode.com/explore/interview/card/microsoft/32/linked-list/212/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        h = set()
        while headA:
            h.add(headA)
            headA = headA.next
        
        while headB:
            if headB in h:
                return headB
            headB = headB.next


a1 = ListNode(4)
a2 = ListNode(1)
i1 = ListNode(8)
b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(1)
i2 = ListNode(4)
i3 = ListNode(5)

a1.next = a2
a2.next = i1
b1.next = b2
b2.next = b3
b3.next = i1
i1.next = i2
i2.next = i3


print (getIntersectionNode(a1,b1))


            