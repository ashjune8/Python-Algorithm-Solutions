
import sys


#arr = []
#for arr_i in xrange(6):
    #arr_temp = map(int,raw_input().strip().split(' '))
   # arr.append(arr_temp)
arr = [[1 ,1, 1, 0, 0, 0],[0 ,1 ,0 ,0 ,0 ,0],[1 ,1, 1, 0, 0, 0],[0 ,9, 2, -4, -4, 0],[0 ,0, 0, -2, 0, 0],[0 ,0, -1, -2, -4 ,0]]
rowposition = 0
columnposition = 0
currentsum = 0
maxsum = -63
while rowposition < 4:
    while columnposition < 4:
        currentsum = arr[rowposition][columnposition] + arr[rowposition][columnposition+1] + arr[rowposition][columnposition+2] + arr[rowposition+1][columnposition+1] + arr[rowposition+2][columnposition] + arr[rowposition+2][columnposition+1] + arr[rowposition+2][columnposition+2]
        maxsum = max(currentsum,maxsum)
        columnposition += 1
    columnposition = 0

    rowposition += 1

print maxsum

