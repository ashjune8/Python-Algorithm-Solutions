def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """



    checkstring = ''

    if len(s) == 0 or len(s) == 1:
        return False

    if len(set(s))==1:
        return True

    else:
        checkstring = s[:len(s)/2]
        if checkstring + checkstring == s:
            return True
        else:
            checkstring = s[:len(s)/3]
            if checkstring+checkstring+checkstring == s:
                return True
    return False




print repeatedSubstringPattern("bacbacbac")
