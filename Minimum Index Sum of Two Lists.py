def findRestaurant(list1, list2):

    setlist1 = set(list1)
    setlist2 = set(list2)
    resultdict = {}
    indexsum = 0
    sumlist = []

    i = 0
    result = list(setlist1 & setlist2)

    while i < len(result):
        indexsum = list1.index(result[i]) + list2.index(result[i])
        if resultdict.has_key(indexsum):
            resultdict[indexsum].append(result[i])

        else:
            resultdict[indexsum] = []
            resultdict[indexsum].append(result[i])

        sumlist.append(indexsum)
        i+=1


    sumlist = sorted(sumlist)

    return resultdict[sumlist[0]]

print findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Burger King","Tapioca Express","Shogun"])


