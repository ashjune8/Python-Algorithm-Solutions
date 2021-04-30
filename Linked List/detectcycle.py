# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

def detectLoop(self, head):
        #code here
        lst = []
        nextNode = head
        while (nextNode.next != None):
            
            if(nextNode in lst):
                return 1
            else:
                lst.append(nextNode)
            nextNode = nextNode.next
        return 0
        