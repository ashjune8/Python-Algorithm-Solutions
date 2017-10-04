def arrayPairSum(nums):
    nums.sort()
    length = len(nums)
    newlst = []
    if length == 2:
        return nums[0]
    else:
        for i in range(length):
            if i % 2 == 0:
                newlst.append(nums[i])

        return sum(newlst)


print arrayPairSum([9,1,5,6,7,2])
