"""Problem No: 219
Problem Name: Contains Duplicate II
Difficulty: Easy
"""
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}

        for i in range(len(nums)):
            if nums[i] in last_index:
                if i - last_index[nums[i]] <= k:
                    return True

            last_index[nums[i]] = i

        return False


sol = Solution()

print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))

