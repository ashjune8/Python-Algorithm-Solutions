def findMedianSortedArrays(nums1, nums2):

    comblist = []
    comblist = nums1 + nums2

    comblist.sort()
    m1 = 0.0
    m2 = 0.0

    if len(comblist)%2 == 0:
        m1 = comblist[len(comblist)/2]
        m2 = comblist[len(comblist)/2 - 1]

        return ((m1 + m2)/float(2))

    else:
        return comblist[(len(comblist)+1)/2 -1]

print findMedianSortedArrays([1,2],[3,4])


