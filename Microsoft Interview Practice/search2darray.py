# https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/154/

from operator import truediv


def searchMatrix(matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = 0
        lastColumn = len(matrix[0])-1

        while row < len(matrix):
            if target <= matrix[row][lastColumn] and target >= matrix[row][0]:
                for i in range(len(matrix[row])):
                    if target == matrix[row][i]:
                        return True
                return False
            elif target >= matrix[row][lastColumn]:
                row += 1
            else:
                return False

        return False

print (searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))