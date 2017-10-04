class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def InsertNth(head, data, position):

    currentposition = 0
    currentnode = head
    previousnode = head
    insertnode = Node(data)
    if position == 0:
        insertnode.next = head
        return insertnode

    while currentposition != position:
        currentposition += 1
        previousnode = currentnode
        currentnode = currentnode.next
    previousnode.next = insertnode
    insertnode.next = currentnode
    return head

a = Node(5)
b = InsertNth(a,3,0)
c = InsertNth(b,5,1)
d = InsertNth(c,4,2)
e = InsertNth(d,2,3)
f = InsertNth(e,10,1)
print e.next.data


