# https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/258/

def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        finalList = sorted(nums1[0:m] + nums2)

        for i in range(len(nums1)):
            nums1[i] = finalList[i]