def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """

    if len(nums) == 0:
        return nums
    start = nums[0]
    previous = nums[0]
    current = nums[0]
    result = []

    i = 0
    while i<len(nums):
        if current in nums:
            previous = current
            current = current+1
            i = i+1
        else:
            if start == previous:
                result.append(str(start))
                start = nums[i]
                previous = nums[i]
                current = nums[i] + 1
                i = i + 1

            else:
                result.append(str(start)+'->'+str(previous))
                start = nums[i]
                previous = nums[i]
                current = nums[i] + 1
                i = i+1
    if start == previous:
        result.append(str(start))
    else:
        result.append(str(start) + '->' + str(previous))




    return result

print summaryRanges([-1])