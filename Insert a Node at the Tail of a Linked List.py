class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Insert(head, data):

    tempnode = Node(data)
    if head == None:
        return tempnode
    root = head
    while root.next != None:
        root = root.next

    root.next = tempnode
    return head