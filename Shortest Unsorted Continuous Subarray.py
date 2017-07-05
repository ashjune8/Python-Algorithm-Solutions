def findUnsortedSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sortedarray = sorted(nums)
    left = 0
    right = len(nums)-1
    while left < right:
        if sortedarray[left]== nums[left]:
            left += 1
        if sortedarray[right]== nums[right]:
            right -= 1
        if sortedarray[left]!= nums[left] and sortedarray[right]!= nums[right]:
            return right - left +1
    return 0


print findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])