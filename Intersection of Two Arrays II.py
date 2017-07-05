def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    result = []
    intersection = list(set(nums1) & set(nums2))
    i = 0
    count = 0
    while i < len(intersection):
        if nums1.count(intersection[i]) == nums2.count(intersection[i]):
           count =  nums1.count(intersection[i])
           while count >0:
               result.append(intersection[i])
               count -= 1
           count = 0
        elif nums1.count(intersection[i]) > nums2.count(intersection[i]):
            count = nums2.count(intersection[i])
            while count > 0:
                result.append(intersection[i])
                count -= 1
            count = 0
        else:
            count = nums1.count(intersection[i])
            while count > 0:
                result.append(intersection[i])
                count -= 1
            count = 0
        i += 1
    return result

print intersect([1, 2, 2, 1],[2,2])
