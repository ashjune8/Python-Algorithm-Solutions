import math

def solution(A):
    radiusset = set()
    for i in range(len(A)):
            temp = A[i].x**2 +  A[i].y**2 +  A[i].z**2
            radiusset.add(temp)

    return len(radiusset)