# https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/257/

def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        setList = set(nums)
        setList = list(setList)
        setList = sorted(setList)

        for i in range(len(nums)):
            if i < len(setList):
                nums[i] = setList[i]
            else:
                nums[i] = '_'
        return len(setList)

print (removeDuplicates([-1,0,0,0,0,3,3]))
