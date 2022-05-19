from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        result = [key for key, value in sorted(count.items(), key=lambda x: x[1], reverse=True)][:k]

        return result


# test
nums = [1, 1, 1, 2, 2, 2, 2, 3]  # [1, 2]
k = 2
nums_1 = [1]  # [1]
k_1 = 1

Ex = Solution()
print(Ex.topKFrequent(nums, k))
