def insertionSort(ar):
    temp = ar[len(ar)-1]
    for i in range(len(ar)-2,-1,-1):
        if ar[i] > temp:
            ar[i+1] = ar[i]
            sarr = [str(a) for a in ar]
            print " ".join(sarr)
        else:
            ar[i+1] = temp
            sarr = [str(a) for a in ar]
            print " ".join(sarr)
            break
    if temp not in ar:
        ar[0] = temp
        sarr = [str(a) for a in ar]
        print " ".join(sarr)


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)