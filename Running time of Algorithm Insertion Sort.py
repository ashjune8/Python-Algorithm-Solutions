def insertionSort(ar,temp,end, shift):
    switch = 0
    for i in range(end-1, -1, -1):
        if ar[i] > temp:
            switch = ar[i+1]
            ar[i + 1] = ar[i]
            ar[i] = switch
            shift += 1

        else:
            ar[i + 1] = temp
            break
    if temp not in ar:
        ar[0] = temp
        shift += 1
        return shift
    else:
        return shift


m = input()
ar = [int(i) for i in raw_input().strip().split()]

#ar = [2,1,3,1,2]
i = 0
shift = 0
while i < len(ar)-1:
    if ar[i] > ar[i+1]:
        shift = insertionSort(ar,ar[i+1],i+1,shift)


    i += 1
print shift