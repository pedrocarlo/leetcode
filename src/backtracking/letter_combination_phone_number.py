# 17. Letter Combinations of a Phone Number

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        n = len(digits)
        if n == 0:
            return output
        combination_map = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z"),
        }

        def backtrack(start: int, curr: str):
            if len(curr) == n:
                output.append(curr)
                return
            for i in range(start, n):
                for char in combination_map[digits[i]]:
                    backtrack(i + 1, curr + char)

        backtrack(0, "")
        return output
