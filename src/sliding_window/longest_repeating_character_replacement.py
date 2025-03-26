# 424. Longest Repeating Character Replacement
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        max_length = 0
        left = 0

        for right in range(len(s)):
            freqs[s[right]] += 1
            max_freq = max(freqs.values())
            curr_len = right - left + 1

            if curr_len - max_freq > k:
                freqs[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


sol = Solution()

res = sol.characterReplacement("AABABBA", 1)
print(res)
