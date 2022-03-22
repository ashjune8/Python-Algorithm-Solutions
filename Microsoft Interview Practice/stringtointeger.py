# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/171/

def myAtoi(str):

    mapping = '0123456789'
    finalString = ''
    minusSigns = 0
    plusSigns = 0
    for i in range(len(str)):
        if str[i] == '-':
            minusSigns += 1
        if str[i] == '+':
            plusSigns += 1
        if minusSigns > 0 and plusSigns>0:
            return 0
        if str[i] in mapping:
            finalString = finalString + str[i]
        elif str[i] == ' ' or str[i] == '-' or str[i] == '+':
            continue
        else:
            break

    if finalString == '':
        return 0
    if minusSigns > 0 and minusSigns%2 != 0:
        finalString = '-' + finalString
    if int(finalString) <= -2147483648:
        return -2147483648
            
    if int(finalString) >= 2147483648:
        return 2147483647
    return int(finalString)