def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    s = sorted(s)
    t = sorted(t)

    i =0

    while i < len(t)-1:
        if s[i] != t[i]:
            return t[i]
        i +=1;
    return t[len(t)-1]


print findTheDifference('a','aa')