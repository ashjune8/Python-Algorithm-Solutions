# https://leetcode.com/explore/interview/card/microsoft/32/linked-list/205/
# Definition for singly-linked list.
from typing import final


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        firstNum = ''
        secondNum = ''
        

        temp = l1
        while temp != None:
            firstNum = firstNum + str(temp.val)
            temp = temp.next

        temp = l2
        while temp != None:
            secondNum = secondNum + str(temp.val)
            temp =  temp.next

        finalNum = str(int(firstNum) + int(secondNum))

        finalList = []
        for i in range(len(finalNum)):
            finalList.append(ListNode(finalNum[i]))

        for i in range(len(finalList)-1):
            finalList[i].next = finalList[i+1]

        return finalList[0]
