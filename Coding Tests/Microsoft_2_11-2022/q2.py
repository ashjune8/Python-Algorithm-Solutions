import re


def solution(A):
    reversedList = A[::-1]
    results = []

    for i in range(len(A)):
        results.append(abs((len(A)-1 - reversedList.index(A[i])) - i))

    return sorted(results)[len(results)-1]

        


print(solution([4,1,2,2,6,6,1]))