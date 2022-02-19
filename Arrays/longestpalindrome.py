# https://www.interviewbit.com/problems/longest-palindromic-substring/

def longestPalindrome(A):

    i = 0
    maxStr = ''
    while i < len(A):
        for j in range(i,len(A)):
            teststr = A[i:j+1]
            if(teststr == teststr[::-1]):
                if(len(teststr) > len(maxStr)):
                    maxStr = teststr
        i += 1
    return maxStr




print longestPalindrome('cbbd')