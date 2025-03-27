# 567. Permutation in String


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        char_count_s2 = dict()
        char_count_s1 = dict()
        for i in range(len(s1)):
            char_count_s1[s1[i]] = char_count_s1.get(s1[i], 0) + 1
            char_count_s2[s2[i]] = char_count_s2.get(s2[i], 0) + 1

        if char_count_s1 == char_count_s2:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            # print(
            #     "start", char_count_s1, char_count_s2, left, s2[left], right, s2[right]
            # )
            char_count_s2[s2[right]] = char_count_s2.get(s2[right], 0) + 1
            char_count_s2[s2[left]] -= 1

            # Delete key so that equality works
            if char_count_s2[s2[left]] == 0:
                del char_count_s2[s2[left]]

            left += 1
            # print("after", char_count_s1, char_count_s2)

            if char_count_s1 == char_count_s2:
                return True

        return False


sol = Solution()

# res = sol.checkInclusion("ab", "eidbaooo")
# print(res)

# res = sol.checkInclusion("ab", "eidboaoo")
# print(res)

# res = sol.checkInclusion("adc", "dcda")
# print(res)
