def solution(A):
    ans = 0
    for i in range(0, len(A)):
        if A[i] < ans:
            ans = A[i]
    return ans

print solution([-1,2])