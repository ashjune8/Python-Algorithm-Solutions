
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        node = head
        queue = []
        temp = ListNode
        while node!= None:
            queue.append(node)
            node = node.next
        k = k%len(queue)
        if k == 0:
            k = len(queue)

        while k >0:
            temp = queue.pop()
            temp.next = queue[0]
            queue[len(queue)-1].next = None
            queue.insert(0,temp)
            k-=1
        return queue[0]
