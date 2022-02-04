# https://www.hackerrank.com/challenges/reverse-a-linked-list/problem?isFullScreen=true

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def reverse(llist):
    # Write your code here

    reverselst = []

    while(llist != None):
        reverselst.append(llist)
        llist = llist.next
    
    reverselst = reverselst[::-1]

    for i in range(len(reverselst)-1):
        reverselst[i].next = reverselst[i+1]

    reverselst[len(reverselst)-1].next = None

    return reverselst[0]
