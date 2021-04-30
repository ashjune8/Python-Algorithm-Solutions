def solution(A):
    # write your code in Python 3.6
    ans = 1
    if (len(A) == 0):
        return None
    for i in range(len(A)):
        ans = ans*A[i]

    if(ans > 1):
        return 1
    elif (ans == 0):
        return 0
    else:
        return -1

print solution([])

