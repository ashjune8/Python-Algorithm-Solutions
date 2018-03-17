def shortestpalindrome(s):
    i = 0
    lst = []
    while i < len(s)-1:
        for j in range(i+1,len(s)):
            if s[i:j+1] == s[j:i-1:-1]:
                lst.append(s[i:j+1])
        i+=1
    return lst
print shortestpalindrome('asasbabbb')

