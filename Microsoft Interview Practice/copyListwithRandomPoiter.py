# https://leetcode.com/explore/interview/card/microsoft/32/linked-list/168

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return head
        originalNodes = []
        nodeList = []
        randomIndexList = []
        finalNodeList = []
        temp = head
        while temp != None:
            nodeList.append(temp.val)
            originalNodes.append(temp)
            temp = temp.next
        
        for i in range(len(originalNodes)):
            if (originalNodes[i].random == None):
                randomIndexList.append(None)
            else:
                randomIndexList.append(originalNodes.index(originalNodes[i].random))

        for i in range(len(nodeList)):
            finalNodeList.append(Node(nodeList[i]))
        
        for i in range(len(nodeList)-1):
            finalNodeList[i].next = finalNodeList[i+1]

            if randomIndexList[i] != None:
                finalNodeList[i].random = finalNodeList[randomIndexList[i]]

        finalNodeList[len(finalNodeList)-1].next = None
        if randomIndexList[len(randomIndexList)-1] != None:
            finalNodeList[len(finalNodeList)-1].random = finalNodeList[randomIndexList[len(randomIndexList)-1]]

        return finalNodeList[0]

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
a.random = b
b.next = c

print (copyRandomList(a))





        
