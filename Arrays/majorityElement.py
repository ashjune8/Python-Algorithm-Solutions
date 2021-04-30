# https://www.interviewbit.com/problems/majority-element/
import math

def majorityElement(A):
    dict = {}

    for i in range(len(A)):
        if(A[i] not in dict.keys() ):
            dict[A[i]] = 1
        else: 
            dict[A[i]] += 1

    for i in dict.keys():
        if(dict[i] > len(A)/2):
            return i
            

print majorityElement([100])