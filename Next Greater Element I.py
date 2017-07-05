def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    result = []

    i = 0
    j = 0
    while i < len(findNums):

        if nums.index(findNums[i]) + j == len(nums) - 1:
            result.append(-1)
            i += 1
            j = 0
        elif nums[nums.index(findNums[i])+j+1] > findNums[i]:
            result.append(nums[nums.index(findNums[i])+j+1])
            i += 1
            j = 0
        else:
             j += 1


    return result

print nextGreaterElement([1,3,5,2,4]
,[6,5,4,3,2,1,7])