class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def FindMergeNode(headA, headB):

    linkedlistA = []
    linkedistB = []

    while headA != None:
        linkedlistA.append(headA.data)
        headA = headA.next

    while headB != None:
        linkedistB.append(headB.data)
        headB = headB.next

    for i in range(len(linkedlistA)):
        if linkedlistA[i] in linkedistB:
            return linkedlistA[i]



