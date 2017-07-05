def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """


    stringarray = s.split()
    if stringarray == []:
        return ''
    if len(stringarray) == 1:
        return stringarray[0]
    reversestring = stringarray[len(stringarray)-1]
    for i in range(len(stringarray)-2,-1,-1):
        reversestring = reversestring + ' ' + stringarray[i]



    return reversestring

print reverseWords('  a  b  ')