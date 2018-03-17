def findpairs(arr):
    lst = []
    for i in range(len(arr)):
        if (10-arr[i]) in arr:
            lst.append((arr[i],10-arr[i]))
    return list(set(lst))

print findpairs([5,5,7,3,4,6,8,9])