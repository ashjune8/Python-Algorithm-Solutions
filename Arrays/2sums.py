# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    leftPointer = 0
    rightPointer = 1

    while leftPointer != len(nums):
        if nums[leftPointer] + nums[rightPointer] == target:
            return [leftPointer,rightPointer]
        elif rightPointer == len(nums) - 1:
            leftPointer += 1
            rightPointer = leftPointer + 1
        else:
            rightPointer += 1

    return None

print (twoSum([3,2,4],6))
