# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/187/

def reverseString(s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) <= 0:
            return s

        temp = ''
        

        leftPointer = 0
        rightPointer = len(s)-1

        while leftPointer != rightPointer and leftPointer < rightPointer:
            temp = s[leftPointer]
            s[leftPointer] = s[rightPointer]
            s[rightPointer] = temp
            leftPointer += 1
            rightPointer -= 1

        return s

print (reverseString(['a','b','c']))
        