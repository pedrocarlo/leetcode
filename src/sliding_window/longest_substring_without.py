# 3. Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        max_length = 0
        left = 0
        for right in range(len(s)):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1

            hash_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
