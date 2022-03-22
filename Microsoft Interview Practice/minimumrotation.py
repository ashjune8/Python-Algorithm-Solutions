# https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/206/

def findMin(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedList = sorted(nums)

        return sortedList[0]

print (findMin([3,4,5,1,2]))

        