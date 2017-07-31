
def lengthOfLongestSubstring(s):

    stringset = set()
    maxlen = 0
    i =0
    j = 0
    while(i<len(s) and j<len(s)):
        if (s[j] not in stringset):
            stringset.add(s[j])
            maxlen = max(maxlen,j+1-i)
            j = j+1

        else:
            tempchar = s[j]
            s = s[i:]
            temp = s.index(tempchar)
            j = temp + 1
            i = temp + 1
            stringset.clear()

    return maxlen






print lengthOfLongestSubstring("ohomm")

