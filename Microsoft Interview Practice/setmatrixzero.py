# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/203/

def setZeroes(matrix):
    rows = []
    columns = []
    maxrows = len(matrix)
    maxcolumns = len(matrix[0])
    steps = maxrows*maxcolumns
    currRow = 0
    currColumn = 0

    while steps != 0:
        if 0 == matrix[currRow][currColumn]:
            rows.append(currRow)
            columns.append(currColumn)
        if currRow < maxrows and currColumn < maxcolumns - 1:
            steps -= 1
            currColumn += 1
        elif currRow < maxrows and currColumn == maxcolumns -1:
            steps -= 1
            currRow += 1
            currColumn = 0
        else:
            continue

    
    rows = list(set(rows))
    columns = list(set(columns))

    for i in range(len(rows)):
        matrix[rows[i]] = [0]*len(matrix[0])

    while len(columns) != 0:
        temp = columns.pop()
        for i in range(len(matrix)):
            matrix[i][temp] = 0

    return matrix

print (setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))