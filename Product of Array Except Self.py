def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    position = 0
    product = 1
    result = []
    i = 0
    while i< len(nums):
        if i == position and position == len(nums) -1:
            result.append(product)
            return result

        if i == position and position != len(nums)-1:
            i += 1
            continue
        if i == len(nums)-1 and position != len(nums) -1:
            product *= nums[i]
            result.append(product)
            product = 1
            i = 0
            position += 1
        else:
            product *= nums[i]
            i += 1


print productExceptSelf([1,2,3,4])



