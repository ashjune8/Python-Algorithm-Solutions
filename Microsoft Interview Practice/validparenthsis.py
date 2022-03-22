# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/179/

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """

        mapping = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
        }

        stack = []

        i = 0
        temp = ''

        for i in range(len(s)):
            if s[i] in mapping:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if s[i] == mapping[temp]:
                    continue
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True

print (isValid(']'))