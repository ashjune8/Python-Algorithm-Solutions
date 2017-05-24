# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = 0
        second = 0
        i = 0
        done = False
        while not done:
            if l1.next == None:
                first += l1.val * 10 ** i
                break
            first += l1.val * 10 ** i
            l1 = l1.next
            i += 1
        i = 0
        while not done:
            if l2.next == None:
                second += l2.val * 10 ** i
                break
            second += l2.val * 10 ** i
            l2 = l2.next
            i += 1
        i = 0
        sum = first + second

        string = str(sum)
        l3 = ListNode
        for i in range(len(string) - 1, 0, -1):
            if i == 0:
                l3 = ListNode(int(string[i]))
                l3.next = None
            else:
                l3 = ListNode(int(string[i]))
                l3.next = ListNode(int(string[i - 1]))
                l3 = l3.next

        return l3