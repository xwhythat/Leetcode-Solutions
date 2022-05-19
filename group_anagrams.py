from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())


# test
strs_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]  # [["bat"],["nat","tan"],["ate","eat","tea"]]
strs_2 = [""]  # [[""]]
strs_3 = ["a"]  # [["a"]]

Ex = Solution()
print(Ex.groupAnagrams(strs_1))
