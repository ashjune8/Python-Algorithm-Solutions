def mostfrequent(arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            dic[arr[i]] += 1

    maximum = 0
    maxkey = 0
    for i in dic:
        if dic[i] > maximum:
            maxkey = i
            maximum = dic[i]

    return maxkey


arr = [1,1,1,2,3,4,4,4,4,4]

print mostfrequent(arr)
