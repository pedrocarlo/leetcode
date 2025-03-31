# https://www.fastprep.io/problems/citadel-get-recommended-friends

from typing import List
from collections import deque


class Node:
    def __init__(self, val: int, neigh: List["Node"] | None = None):
        self.val = val
        self.neigh = neigh if neigh else []


class Solution:
    def getRecommendedFriends(self, n: int, friendships: List[List[int]]) -> List[int]:
        adj: list[set[int]] = [set() for _ in range(n)]

        for first, second in friendships:
            adj[first].add(second)
            adj[second].add(first)

        # max common ancestor
        def search_friend(root: int) -> int:
            freq: dict[int, int] = dict()
            friends = adj[root].copy()

            for friend in friends:
                second_degree_friends = adj[friend]

                for second_friend in second_degree_friends:
                    if second_friend != root and second_friend not in friends:
                        if second_friend not in freq:
                            freq[second_friend] = 0
                        freq[second_friend] += 1

            max_rec_count = 0
            max_rec_idx = -1
            for rec, count in freq.items():
                if count > max_rec_count:
                    max_rec_count = count
                    max_rec_idx = rec
                elif count == max_rec_count and rec < max_rec_idx:
                    max_rec_count = count
                    max_rec_idx = rec

            return max_rec_idx if max_rec_idx >= 0 else -1

        return [search_friend(user) for user in range(n)]


sol = Solution()
# res = sol.getRecommendedFriends(5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]])
# [3, 2, 1, 0, 1]
# print(res)

# res = sol.getRecommendedFriends(3, [[0, 1], [1, 2], [2, 0]])
# [-1, -1, -1]
# print(res)
