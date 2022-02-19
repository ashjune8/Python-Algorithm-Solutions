# https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome(s):
    maxlen = 0;
    maxstr = '';

    

    for i in range(0, len(s)):
        result = traverseString(s[i:len(s)], maxlen, maxstr)
        maxlen = result['maxlen']
        maxstr = result['maxstr']

    return maxstr

def traverseString(st, maxl, maxst):
        s = st
        maxlen = maxl
        maxstr = maxst

        for i in range(len(s)):
            temparr = s[i:len(s)]
            if temparr == temparr[::-1]:
                if len(temparr) > maxlen:
                    maxstr = temparr
                    maxlen = len(temparr)
        
        for i in range(len(s), -1, -1):
            temparr = s[0:i]
            if temparr == temparr[::-1]:
                if len(temparr) > maxlen:
                    maxstr = temparr
                    maxlen = len(temparr)

        return {
            'maxlen': maxlen,
            'maxstr': maxstr
        }




        

    




    


print (longestPalindrome('cbbd'))

