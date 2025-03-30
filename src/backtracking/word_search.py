# 79. Word Search

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_len = len(word)
        rows = len(board)
        cols = len(board[0])
        visited: set[tuple[int, int]] = set()

        def backtrack(row: int, col: int, char_count: int):
            if char_count == word_len:
                return True
            # Check if in bounds
            # not already visited
            # and if the character is in the correct location
            if (
                not (0 <= row < rows)
                or not (0 <= col < cols)
                or (row, col) in visited
                or board[row][col] != word[char_count]
            ):
                return False

            visited.add((row, col))
            new_count = char_count + 1
            res = (
                backtrack(row + 1, col, new_count)
                or backtrack(row - 1, col, new_count)
                or backtrack(row, col + 1, new_count)
                or backtrack(row, col - 1, new_count)
            )

            visited.remove((row, col))
            return res

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        return False
