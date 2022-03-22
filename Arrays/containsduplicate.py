# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    
    leftPointer = 0
    rightPointer = 1

    if len(nums) <= 1:
        return False
    nums = sorted(nums)
    while rightPointer <= len(nums)-1:
        if nums[leftPointer] == nums[rightPointer]:
            return True
        leftPointer += 1
        rightPointer += 1
    
    return False

print (containsDuplicate([1,2,3]))
