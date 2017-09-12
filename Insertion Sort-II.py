def insertionSort(ar,temp,end):
    switch = 0
    for i in range(end - 1, -1, -1):
        if ar[i] > temp:
            switch = ar[i + 1]
            ar[i + 1] = ar[i]
            ar[i] = switch

        else:
            ar[i + 1] = temp
            break
    if temp not in ar:
        ar[0] = temp
        sarr = [str(a) for a in ar]
        print " ".join(sarr)
        return ar
    else:
        sarr = [str(a) for a in ar]
        print " ".join(sarr)
        return ar


m = input()
ar = [int(i) for i in raw_input().strip().split()]


i = 0
while i < len(ar)-1:
    if ar[i] > ar[i+1]:
        ar = insertionSort(ar,ar[i+1],i+1)

    else:
        sarr = [str(a) for a in ar]
        print " ".join(sarr)
    i += 1
