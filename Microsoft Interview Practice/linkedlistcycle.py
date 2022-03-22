class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):

    temp = head
    listofNodes = []

    while temp != None:
        if temp in listofNodes:
            return True
        listofNodes.append(temp)
        temp = temp.next

    return False