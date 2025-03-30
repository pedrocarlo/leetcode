# 131. Palindrome Partitioning

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str) -> bool:
            if not s:
                return False
            word_len = len(s)
            first = 0
            last = word_len - 1
            while first < last:
                if s[first] != s[last]:
                    return False
                first += 1
                last -= 1
            return True

        self.output = []
        word_len = len(s)

        def backtrack(start: int, curr: List[str]):
            if start == word_len:
                self.output.append(curr[:])
                return

            for end in range(start + 1, len(s) + 1):
                # simpler approach. Check here before backtraking
                if is_palindrome(s[start:end]):
                    backtrack(end, curr + [s[start:end]])

        backtrack(0, [])
        return self.output
