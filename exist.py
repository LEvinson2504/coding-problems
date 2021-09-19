from typing import List

# Notes:
# might only take first occurence of char in consideration


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # print(self.findIJ("S", board))
        i, j = self.findIJ(word[0], board)
        # flag = 0
        for k in range(1, len(word) - 1):
            i, j = self.findAdj(word[k], i, j, board)
            if i == -1:
                return False
        return True
        # print(board[0][1])

    def findIJ(self, ch: str, board: List[List[str]]) -> List[int]:
        for i in range(len(board)):
            if ch in board[i]:
                return [i, board[i].index(ch)]
        return [-1, -1]

    def findAdj(self, chToFind: str, i: int, j: int, board: List[List[str]]):
        ci, cj = self.findIJ(chToFind, board)
        if abs(ci - i) == 1 and abs(cj - j) == 1:
            return [ci, cj]
        else:
            return [-1, -1]


solve = Solution()
print(solve.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"],
                         ["A", "D", "E", "E"]], word="ABCCED"))
