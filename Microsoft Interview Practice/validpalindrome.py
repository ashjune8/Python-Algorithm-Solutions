# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/162/

def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """

        alphanum = 'abcdefghijklmnopqrstuvwxyz0123456789'

        result = ''

        for i in s:
            match = i.lower()
            if match in alphanum:
                result += match
        if result == result[::-1]:
            return True
        return False

        

print (isPalindrome("0P"))
