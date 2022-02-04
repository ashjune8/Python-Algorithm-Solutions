# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem?isFullScreen=true

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def mergeLists(head1, head2):

    lst1 = []
    lst2 = []
    lst3 = []

    while head1 != None:
        lst1.append(head1.data)
        head1 = head1.next
    
    while head2 != None:
        lst2.append(head2.data)
        head2 = head2.next

    lst3 = lst1 + lst2
    lst3 = sorted(lst3)

    finallst = []

    for i in range(len(lst3)):
        finallst.append(SinglyLinkedListNode(lst3[i]))

    for i in range(len(finallst) -1):
        finallst[i].next = finallst[i+1]

    return finallst[0]
