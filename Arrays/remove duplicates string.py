
def removeDuplicates(s):
    
    # code here
    newString = ""
    i = 0
    
    while (i < len(s)):
        if (newString.find(s[i]) == -1 ):
            a = s[i+1:len(s)]
            b = s[i]
            newString = newString + s[i]
        i +=1
            
    return newString

print removeDuplicates('bcabc')