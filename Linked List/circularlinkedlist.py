# https://practice.geeksforgeeks.org/problems/circular-linked-list/1/

class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

def isCircular(head):
    # Code here

    if(head == None):
        return 1

    accessedNodes = []
    tempNode = head
    
    while(tempNode != None):
        if(tempNode not in accessedNodes):
            accessedNodes.append(tempNode)
        else:
            return 1
        tempNode = tempNode.next
    
    return 0

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = a

print (isCircular(a))


