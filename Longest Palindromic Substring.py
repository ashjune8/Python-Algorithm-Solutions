def longestPalindrome(s):

    position = 0
    palindrome = ''
    current = ''
    maxpalindrome = ''
    while position < len(s):

        for i in range(position,len(s)):
            palindrome += s[i]

            if palindrome == palindrome[::-1]:
                current = palindrome
                if len(current) > len(maxpalindrome):
                    maxpalindrome = current


        palindrome = ''
        current = ''
        position += 1

    return maxpalindrome

print longestPalindrome("babad")


