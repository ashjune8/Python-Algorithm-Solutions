class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def CompareLists(headA, headB):

    while headA != None and headB != None:

        if headA.data != headB.data:
            return 0
        headA = headA.next
        headB = headB.next
    if headA == None and headB == None:
        return 1
    return 0



