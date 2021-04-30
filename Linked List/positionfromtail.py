# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def getNode(head, positionFromTail):
    if head == None:
        return head
    lst = []

    while head != None:
        lst.append(head.data)
        head = head.next
    
    lst = lst[::-1]
    return lst[positionFromTail]



