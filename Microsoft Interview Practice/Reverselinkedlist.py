# https://leetcode.com/explore/interview/card/microsoft/32/linked-list/169/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    listofNodes = []
    temp = head

    if head == None or head.next == None:
        return head

    while temp != None:
        listofNodes.append(temp)
        temp = temp.next

    listofNodes = listofNodes[::-1]

    for i in range(len(listofNodes)-1):
        listofNodes[i].next = listofNodes[i+1]

    listofNodes[len(listofNodes)-1].next = None

    return listofNodes[0]
