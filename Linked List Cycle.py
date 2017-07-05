#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head == None:
            return False
        start = head
        temp = head
        try:
            while start.next != None and temp.next.next != None:

                start = start.next
                temp = temp.next.next
                if start == temp:
                    return True
            return False
        except:
            return False
