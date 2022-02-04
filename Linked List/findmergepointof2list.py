class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def findMergeNode(head1, head2):

    listOfNodesHead1 = []

    if head1 == None or head2 == None:
        return None

    tempHead1 = head1
    
    while tempHead1.next != None:
        listOfNodesHead1.append(tempHead1)
        tempHead1 = tempHead1.next
        
    listOfNodesHead1.append(tempHead1)

    tempHead2 = head2

    while tempHead2.next != None:
        if tempHead2 in listOfNodesHead1:
            return tempHead2.data
        tempHead2 = tempHead2.next

    if tempHead2 in listOfNodesHead1:
        return tempHead2.data
    return None

a = SinglyLinkedListNode(1)
b = SinglyLinkedListNode(2)
c= SinglyLinkedListNode(3)
d = SinglyLinkedListNode(4)
e = SinglyLinkedListNode(5)

a.next = b
b.next = c
d.next = e
e.next = b

print findMergeNode(a,d)