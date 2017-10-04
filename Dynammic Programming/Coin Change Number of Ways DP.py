import sys

def getWays(n, c):
    # Complete this function

    temp = [[0] * (n+1 )for i in range(len(c)+1)]

    for i in range(len(c)+1):
        temp[i][0] =1

    for i in range(1,len(c)+1):
        for j in range(1,n+1):
            if c[i-1] > j:
                temp[i][j] = temp[i-1][j]
            else:
                temp[i][j] = temp[i][j-c[i-1]] + temp[i-1][j]

    return temp[len(c)][n]

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
c = map(int, raw_input().strip().split(' '))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'

print  getWays(n, c)