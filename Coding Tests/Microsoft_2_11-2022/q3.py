# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    convertedstring = str(N)
    locationoffive = []
    results = []
    maxitem = 0

    if '5' not in convertedstring:
        return None

    for i in range(len(convertedstring)):
        if(convertedstring[i] == '5'):
            locationoffive.append(i)
    for i in range(len(locationoffive)):
        if(locationoffive[i] == 0):
            results.append(int(convertedstring[1:len(convertedstring)]))
        elif (locationoffive[i] == len(convertedstring) - 1):
            results.append(int(convertedstring[0:len(convertedstring)-1]))
        else:
            results.append(int(convertedstring[0:locationoffive[i]] + convertedstring[locationoffive[i]+1:len(convertedstring)]))
    
    maxitem = results[0]
    for i in range(len(results)):
        if results[i] > maxitem:
            maxitem = results[i]

    return maxitem

print (solution(-5000))


    


