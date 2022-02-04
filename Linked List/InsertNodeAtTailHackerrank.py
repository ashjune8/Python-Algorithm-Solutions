class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def insertNodeAtTail(head, data):
    if head == None:
        return SinglyLinkedListNode(data)
    
    tempHead = head

    while tempHead.next != None:
        tempHead = tempHead.next

    tempHead.next = SinglyLinkedListNode(data)
    return head



a = SinglyLinkedListNode(1)
b = SinglyLinkedListNode(2)
c = SinglyLinkedListNode(3)
a.next = b
b.next = c

print insertNodeAtTail(a,4).next.next.next.data