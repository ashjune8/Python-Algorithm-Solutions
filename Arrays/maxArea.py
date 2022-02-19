# https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(heights) - 1
        
        max_area = 0
        
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = height * width
            
            max_area = max(max_area, area)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_area