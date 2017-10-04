def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    currentcount = 0
    maxcount = 0
    i = 0
    while i<len(nums):
        if nums[i] == 1:
            currentcount += 1
        else:
            maxcount = max(maxcount,currentcount)
            currentcount = 0
        i += 1
    return max(maxcount,currentcount)

print findMaxConsecutiveOnes([1])

