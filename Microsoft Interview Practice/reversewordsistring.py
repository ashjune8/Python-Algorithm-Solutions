# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/166/

def reverseWords(s):

    words = s.split()
    words = words[::-1]


    if len(words) == 0:
        return ''
    return ' '.join(words)

print (reverseWords("the sky is  blue"))

    
