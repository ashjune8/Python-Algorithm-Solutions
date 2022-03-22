# https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/193/

def sortColors(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        sortedList = sorted(nums)

        for i in range(len(nums)):
            nums[i] = sortedList[i]