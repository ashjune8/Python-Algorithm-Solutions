import sys




def findnumberoftransmitters(x,k, transmitternumber):
    i =  0

    while i < len(x):
        transmitternumber += 1
        compare = x[i] + k
        while i < len(x) and x[i] <= compare:
            i +=1
        i -= 1
        compare = x[i] + k
        while i < len(x) and x[i] <= compare:
            i +=1
    return transmitternumber






n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
x = map(int,raw_input().strip().split(' '))
#x = [1,2,3,4,5]
#k = 1
i =0
x = sorted(x)
transmitternumber = 0
print findnumberoftransmitters(x,k,transmitternumber)

