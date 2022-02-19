# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentarrsum = nums[0]
        maxarrsum = nums[0]

        if (len(nums) == 1 ):
            return maxarrsum
        else:
            for i in range(1, len(nums)):
                if nums[i] > currentarrsum + nums[i]:
                    currentarrsum = nums[i]
                else:
                    currentarrsum = currentarrsum + nums[i]
                
                if currentarrsum > maxarrsum:
                    maxarrsum = currentarrsum

        return maxarrsum

print (maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



