# https://leetcode.com/problems/minimum-window-substring/

import re


def minWindow(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        leftPointer = 0
        rightPointer = 0
        result = None
        matchFound = True


        while leftPointer != len(s):
            windowsubstring = s[leftPointer:rightPointer+1]
            for i in range(len(t)):
                if t[i] not in windowsubstring:
                    matchFound = False
                    break
                if t[i] in windowsubstring:
                    windowsubstring = windowsubstring.replace(t[i],'',1)
                
            windowsubstring = s[leftPointer:rightPointer+1]
            if matchFound == True:
                if result == None:
                    result = windowsubstring
                if len(windowsubstring) < len(result):
                    result = windowsubstring
                leftPointer += 1
            elif rightPointer != len(s) - 1:
                rightPointer += 1
            else:
                leftPointer += 1
                continue
            
            matchFound = True
        if result == None:
            return ''
        if len(result) < len(t):
            return ''
        
        return result

print (minWindow("cabwefgewcwaefgcf",
"cae"))
            
