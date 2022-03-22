# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/213/

def reverseWords(s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        words = ''.join(s).split()
        words = words[::-1]

        finalString = ' '.join(words)
        return list(finalString)
        
print (reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))