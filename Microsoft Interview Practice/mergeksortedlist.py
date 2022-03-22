# https://leetcode.com/explore/interview/card/microsoft/32/linked-list/209/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    tempList = []
    finalList = []
    finalListNode = []

    if len(lists) == 0:
        return None

    for i in lists:
        temp = i
        while temp != None:
            finalList.append(temp.val)
            temp = temp.next

    finalList = sorted(finalList)
    if len(finalList) == 0:
        return
    for i in finalList:
        finalListNode.append(ListNode(i))

    for i in range(len(finalListNode)-1):
        finalListNode[i].next = finalListNode[i+1]

    return finalListNode[0]

