def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    nums = sorted(nums)

    if len(nums) == 1:
        return nums[0]

    for i in range(1,len(nums)-1):
        if nums[i] == nums[i-1] or nums[i] == nums[i+1]:
            continue
        else:
            return nums[i]

    if nums[0] != nums[1]:
        return nums[0]
    if nums[len(nums)-1] != nums[len(nums)-2]:
        return nums[len(nums)-1]



print singleNumber([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6])