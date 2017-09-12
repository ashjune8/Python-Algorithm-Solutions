def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    Sum = [0]*len(nums)
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    Sum[0] = nums[0]
    Sum[1] = max(nums[0],nums[1])

    for i in range(2,len(nums)):
        Sum[i] = max(Sum[i-1],Sum[i-2] + nums[i])

    return Sum[len(nums)-1]

print rob([0,0])