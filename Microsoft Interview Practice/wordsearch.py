# https://leetcode.com/explore/interview/card/microsoft/46/backtracking/256/

def findWords(board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        finalString = ''
        finalList = []

        for i in range(len(board)):
            finalString = finalString + ''.join(board[i]) + '_'

        i = 0
        j = 0
        while j < len(board[0]):
            finalString = finalString + board[i][j]
            if i == len(board) - 1:
                j = j+ 1
                i = 0
                finalString = finalString + '_'
            else:
                i = i + 1

        for i in words:
            if i in finalString:
                finalList.append(i)

        return finalList

print (findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))



