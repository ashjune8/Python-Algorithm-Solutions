class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None
        self.prevnode = None

def reverselinkedlist(head):
    current = head
    next = head

    while next.nextnode != None:
        temp = next
        next = current.nextnode
        next.prevnode = current
        current = temp

    next.prevnode = current
    current = next


    while current != None:
        print current.value
        current = current.prevnode

a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode = b
b.nextnode = c
print reverselinkedlist(a)

