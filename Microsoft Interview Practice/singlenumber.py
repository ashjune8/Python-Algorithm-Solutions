# https://leetcode.com/explore/interview/card/microsoft/48/others/208/

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