from typing import List


# O(n**2)
def countStableSegments(self, capacity: List[int]) -> int:
    res = 0
    size = len(capacity)
    curr_sum = 0
    prefix_sum = [0] * size
    for i in range(size):
        prefix_sum[i] = curr_sum + capacity[i]
        curr_sum += capacity[i]
        for j in range(i):
            if (
                capacity[i] == capacity[j]
                and prefix_sum[i] - prefix_sum[j] - capacity[i] == capacity[j]
            ):
                res += 1

    return res
