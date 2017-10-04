import sys


#n1,n2,n3 = raw_input().strip().split(' ')
#n1,n2,n3 = [int(n1),int(n2),int(n3)]
#h1 = map(int,raw_input().strip().split(' '))
#h2 = map(int,raw_input().strip().split(' '))
#h3 = map(int,raw_input().strip().split(' '))
h1 = [3,2,1,1,1]
h2 = [4,3,2]
h3 = [1,1,4,1]

l1 = sum(h1)
l2 = sum(h2)
l3 = sum(h3)
temp = 0

while l1 != l2 or l2 != l3 or l3 != l1:
    maximum = max(l1,l2,l3)
    if l1 == maximum:
        temp = h1.pop(0)
        l1 = l1 - temp
    if l2 == maximum:
        temp = h2.pop(0)
        l2 = l2 - temp
    if l3 == maximum:
        temp = h3.pop(0)
        l3 = l3 - temp






print sum(h3)