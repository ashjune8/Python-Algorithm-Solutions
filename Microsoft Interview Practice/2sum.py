# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/173/

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