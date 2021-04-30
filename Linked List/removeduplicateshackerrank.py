# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def removeDuplicates(head):
    tempNode = head
    lst = []
    nodelst = []
    
    

    while tempNode != None:
        if (tempNode.data not in lst):
            lst.append(tempNode.data)
            nodelst.append(tempNode)
            tempNode = tempNode.next
            

            
        else:
            tempNode = tempNode.next
    
    for i in range(len(nodelst)-1):
        nodelst[i].next = nodelst[i+1]
    
    nodelst[len(nodelst)-1].next = None


    return nodelst[0]


