# https://leetcode.com/explore/interview/card/microsoft/32/linked-list/175/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    list1 = []
    list2 = []
    finalListNodes = []
    

    temp = l1

    while temp != None:
        list1.append(temp.val)
        temp = temp.next

    temp = l2
    while temp != None:
        list2.append(temp.val)
        temp = temp.next

    finalList = sorted(list1 + list2)

    if len(finalList) == 0:
        return None
    for i in range(len(finalList)):
        finalListNodes.append(ListNode(finalList[i]))

    for i in range(len(finalListNodes)-1):
        finalListNodes[i].next = finalListNodes[i+1]

    return finalListNodes[0]



    