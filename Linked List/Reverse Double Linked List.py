class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

def Reverse(head):
    curr = head
    lst = []
    if curr == None or curr.next == None:
        return curr
    while curr != None:
        lst.append(curr)
        curr = curr.next

    lst = lst[::-1]
    for i in range(1,len(lst)-1):
        lst[i].next = lst[i+1]
        lst[i].prev = lst[i-1]

    lst[0].prev = None
    lst[0].next = lst[1]
    lst[len(lst)-1].prev = lst[len(lst)-2]
    lst[len(lst) - 1].next = None
    return lst[0]

a = Node(2)
a.next = Node(4)
a.next.next = Node(6)
print Reverse(a).data


