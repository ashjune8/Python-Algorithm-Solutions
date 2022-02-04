# https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1/?company[]=Amazon&company[]=Amazon&page=1&query=company[]Amazonpage1company[]Amazon

class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None


def deleteNode(curr_node):
    if ( curr_node.next != None):
        curr_node.data = curr_node.next.data
        curr_node.next = curr_node.next.next
    else:
        curr_node = None
    

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

deleteNode(b)
print a.data
print a.next.data

