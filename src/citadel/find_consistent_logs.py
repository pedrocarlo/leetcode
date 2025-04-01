# https://www.fastprep.io/problems/citadel-find-consistent-logs


from typing import List
from collections import defaultdict, Counter


class Solution:
    def findConsistentLogs(self, userEvent: List[int]) -> int:
        freq = Counter(userEvent)

        min_freq = min(freq.values())

        def is_consistent(freq: dict[int, int]) -> bool:
            nonlocal min_freq

            most_freq = max(freq.values())

            return most_freq == min_freq

        curr_freq: dict[int, int] = defaultdict(int)
        left = 0
        max_length = 0
        for right in range(len(userEvent)):
            curr_freq[userEvent[right]] += 1

            while left < right and not is_consistent(curr_freq):
                curr_freq[userEvent[left]] -= 1
                left += 1

            if is_consistent(curr_freq):
                max_length = max(max_length, (right - left) + 1)

        return max_length


sol = Solution()
# res = sol.findConsistentLogs([1, 2, 1, 3, 4, 2, 4, 3, 3, 4])
# # 8
# print(res)

res = sol.findConsistentLogs([1, 2, 1, 3, 4, 4, 3, 3, 4, 1])
# 4
print(res)
