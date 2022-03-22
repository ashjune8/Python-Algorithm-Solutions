# https://leetcode.com/explore/interview/card/microsoft/32/linked-list/170/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    firstNumber = ''
    secondNumber = ''
    finalresultlist=[]

    temp = l1

    while temp != None:
        firstNumber = firstNumber + str(temp.val)
        temp = temp.next

    temp = l2
    
    while temp != None:
        secondNumber = secondNumber + str(temp.val)
        temp = temp.next

    firstNumber = int(firstNumber[::-1])
    secondNumber = int(secondNumber [::-1])
    result = str(firstNumber + secondNumber)

    resultList = list(result)
    resultList = resultList[::-1]
    if len(resultList) == 1:
        return ListNode(int(resultList[0]))
    
    
    for i in range(len(resultList)):
        finalresultlist.append(ListNode(int(resultList[i])))

    for i in range(len(finalresultlist)-1):
        finalresultlist[i].next = finalresultlist[i+1]

    return finalresultlist[0]




