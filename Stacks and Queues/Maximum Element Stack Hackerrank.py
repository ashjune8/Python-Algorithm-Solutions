import sys

N = int(sys.stdin.readline())
stack = []
tempread = []
maximum = -sys.maxint-1

#def pushelement(ele,stack):
    #stack.insert(0,ele)

#def deletetopelement(stack):
    #stack.pop(0)

#def printmaxsatckelement(stack):
    #temp = sorted(stack)
    #print temp[len(stack)-1]

for i in range(N):

    tempread = sys.stdin.readline().split()

    if int(tempread[0]) == 1:
        stack.insert(0,int(tempread[1]))
        maximum = max(maximum,stack[0])
    elif int(tempread[0]) == 2:
        if maximum == stack[0]:
            stack.pop(0)
            temp = sorted(stack)[::-1]
            if temp == []:
                maximum = -sys.maxint-1
            else:
                maximum = temp[0]
        else:
            stack.pop(0)



    else:
        print maximum






