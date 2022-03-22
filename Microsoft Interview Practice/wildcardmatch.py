# https://leetcode.com/explore/interview/card/microsoft/46/backtracking/155/

def isMatch(s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def patternCheck(s,p):
            if '*' not in p:
                return False
            else:
                return True



        if len(s) != len(p):
            return patternCheck(s,p)
        else:
            for i in range(len(s)):
                if s[i] == p[i] or p[i] == '?' or p[i] == '*':
                    continue
                else:
                    return False
            return True 

        



print (isMatch('ab','?c'))