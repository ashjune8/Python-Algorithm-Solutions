def solution(A):
    # write your code in Python 3.6
    result = 1
    for i in range(len(A)):
        result = result*A[i]
    
    if result < 0 :
        return -1
    elif result == 0:
        return 0
    else:
        return 1

print (solution([1,2,3,0]))
