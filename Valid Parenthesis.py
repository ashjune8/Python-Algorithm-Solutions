def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    stack = []
    i = 0
    if len(s) == 1 or len(s) == 0 or len(s)%2 !=0:
        return False
    temp = ''
    while i<len(s):
        if s[i] in ['(','{','[']:
            stack.append(s[i])
            i += 1
            continue

        if s[i] in [')','}',']'] and stack != []:
            temp = stack.pop()
            if temp == '(' and s[i] == ')':
                i += 1
                continue
            if temp == '[' and s[i] == ']':
                i += 1
                continue
            if temp == '{' and s[i] == '}':
                i += 1
                continue
        else:
            return False
    return stack == []

print isValid("([)]")








