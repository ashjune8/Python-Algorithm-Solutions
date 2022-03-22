# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/180/

from turtle import left


def longestPalindrome(A):
        """
        :type s: str
        :rtype: str
        """

        maxstr = ''

        leftPointer = 0
        rightPointer = 1

        if A == None or len(A) == 1:
            return A

        while leftPointer != len(A)-1:
            temp = A[leftPointer:rightPointer]
            if len(temp) > len(maxstr) and temp == temp[::-1]:
                maxstr = A[leftPointer:rightPointer]
            if rightPointer == len(A):
                leftPointer += 1
                rightPointer = leftPointer + 1
            else:
                rightPointer += 1

        return maxstr
print (longestPalindrome('babad'))

    