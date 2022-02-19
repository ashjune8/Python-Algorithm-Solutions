# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lst = []
        currentNode = head

        while currentNode != None:
            lst.append(currentNode)
            currentNode = currentNode.next

        nodeIndexToBeRemoved = len(lst) - n
        if nodeIndexToBeRemoved == 0 and len(lst) == 1:
            return None
        elif nodeIndexToBeRemoved == 0:
            return lst[1]
        else:
            lst[nodeIndexToBeRemoved - 1].next = lst[nodeIndexToBeRemoved].next
            return lst[0]

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)



        

