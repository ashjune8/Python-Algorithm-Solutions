def minMoves(nums):

    """
    :type nums: List[int]
    :rtype: int
    """


    difference = 0
    nums = sorted(nums)
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == nums[0]:
            break
        difference += nums[i] - nums[0]

    return difference

print minMoves([1,2,3,4])
