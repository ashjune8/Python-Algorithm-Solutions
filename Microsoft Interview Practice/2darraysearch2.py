# https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/195/

def searchMatrix(matrix, target):

    rows = len(matrix)
    columns = len(matrix[0])
    steps = rows*columns
    currRow = 0
    currColumn = 0

    while steps != 0:
        if target == matrix[currRow][currColumn]:
            return True
        elif currRow < rows and currColumn < columns - 1:
            steps -= 1
            currColumn += 1
        elif currRow < rows and currColumn == columns -1:
            steps -= 1
            currRow += 1
            currColumn = 0
        else:
            return False

    return False

print (searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))

