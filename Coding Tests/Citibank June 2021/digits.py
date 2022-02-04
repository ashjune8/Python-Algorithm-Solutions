def solution(N):
    # write your code in Python 3.6

    stringConverted = str(N)
    resultString = ''

    if(len(stringConverted) == 1):
        return 0
    
    for i in range(len(stringConverted)):
        if (i == 0):
            resultString += '1'
        else:
            resultString += '0'
    
    return int(resultString)

    



print solution(2)